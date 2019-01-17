# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:25:11 2019

@author: kinde
"""

import pandas as pd
import numpy as np

from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing

neigh = KNeighborsRegressor(n_neighbors=2)


maleFV = pd.read_csv("feature_vector_gender_prediction_male.csv", sep="\t")
maleFV = maleFV.drop(maleFV.columns[0], axis=1)

femaleFV = pd.read_csv("feature_vector_gender_prediction_female.csv", sep="\t")
femaleFV = femaleFV.drop(femaleFV.columns[0], axis=1)



maleValues = maleFV.values
femaleDF = pd.DataFrame(data =femaleFV.values, columns= maleFV.columns)

print(femaleDF.head())

mergedDF = pd.concat([maleFV, femaleDF], ignore_index = True)


print(mergedDF.head())
#print(maleFV.shape)


UserInfo = pd.read_csv("LFM-1b_subset_MTAP2018.csv", sep='\t')
UserInfo.columns =['user_id','age','gender','country']

merged_p1 = pd.merge(UserInfo, mergedDF, on='user_id')

user_stats = pd.read_csv("LFM-1b_users_additional.txt", sep='\t')

merged_p2 = pd.merge(user_stats, merged_p1, on='user_id')

print(merged_p2.head(), merged_p2.shape)

merged_p2 = merged_p2.drop(['user_id'], axis=1)

merged_p2.to_csv("WekaTest.csv", sep=",", index=False)
print(merged_p2['gender'])
