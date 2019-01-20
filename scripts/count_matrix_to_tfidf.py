#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:34:33 2019

@author: sztkp
"""

from sklearn.feature_extraction.text import TfidfTransformer
from scipy import sparse

import pandas as pd


######################################################
MATRIX_PATH='data/user_artist_matrix_overall.csv'
OUTPUT_PATH='global.tfidf'
######################################################


######################################################
###READING MATRIX

print("Reading data!")

count_matrix = pd.read_csv(MATRIX_PATH, sep="\t",index_col=1)
count_matrix.drop(count_matrix.columns[0], axis=1,inplace=True)

print("FINISHED reading data!")
print("")

######################################################
###CONVERTING TO SPARSE MATRIX
     
sparse=sparse.csr_matrix(count_matrix.values)

######################################################
###PERFORMING TF-IDF

print("TF-IDF-ing!")

tfidf_transformer = TfidfTransformer(sublinear_tf=True).fit(sparse)
tfidf_matrix = tfidf_transformer.transform(sparse)

print("FINISHED TF-IDF-ing!")
print("")

#####################################################
###CONVERTING SPARSE MATRIX TO ARRAY

tfidf_arrayed=tfidf_matrix.toarray()

#####################################################
###WRITING DATA

print("Writing data!")

tfidf_final=pd.DataFrame(data=tfidf_arrayed,index=count_matrix.index,columns=count_matrix.columns)
tfidf_final.to_csv(OUTPUT_PATH, sep='\t')

print("FINISHED writing data!")