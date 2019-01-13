#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 19:16:29 2019

@author: sztkp
"""

import numpy as np
import pandas as pd


USERS_FILTER_PATH='data/LFM-1b_subset_MTAP2018.csv'
LE_DATA_PATH='data/LFM-1b_LEs.txt'


def read_data():
    user_subset =pd.read_csv(USERS_FILTER_PATH, sep="\t", header=0)
    
    user_subset.columns = ['user_id','age','gender','country']
    
    return user_subset

##returns a list with the users filtered in age bins
##first element of the list contains description of the groups
def get_age_bins():
    
    user_subset=read_data()
    
    bins=["6-17","18-21","22-25","26-30","31-40","41-50","51-60","61-100"]
    
    b6_17=user_subset[user_subset['age'].isin(range(6,18))]
    b18_21=user_subset[user_subset['age'].isin(range(18,22))]
    b22_25=user_subset[user_subset['age'].isin(range(22,26))]
    b26_30=user_subset[user_subset['age'].isin(range(26,31))]
    b31_40=user_subset[user_subset['age'].isin(range(31,41))]
    b41_50=user_subset[user_subset['age'].isin(range(41,51))]
    b51_60=user_subset[user_subset['age'].isin(range(51,61))]
    b61_100=user_subset[user_subset['age'].isin(range(61,101))]
    
    return [bins,b6_17,b18_21,b22_25,b26_30,b31_40,b41_50,b51_60,b61_100]
    
if __name__ == '__main__':

    age=get_age_bins()

    b6_17=age[1]["user_id"].tolist()
    b18_21=age[2]["user_id"].tolist()
    b22_25=age[3]["user_id"].tolist()
    b26_30=age[4]["user_id"].tolist()
    b31_40=age[5]["user_id"].tolist()
    b41_50=age[6]["user_id"].tolist()
    b51_60=age[7]["user_id"].tolist()
    b61_100=age[8]["user_id"].tolist()
    
    topArtists_helper = pd.DataFrame() #Empty dataframe to store the users with their corresponding playcount
    topArtists = pd.DataFrame()
    
    top_artists_b6_17=pd.DataFrame()
    top_artists_b18_21=pd.DataFrame()
    top_artists_b22_25=pd.DataFrame()
    top_artists_b26_30=pd.DataFrame()
    top_artists_b31_40=pd.DataFrame()
    top_artists_b41_50=pd.DataFrame()
    top_artists_b51_60=pd.DataFrame()
    top_artists_b61_100=pd.DataFrame()

    chunksize=50000
    counter=0
    
    for chunk in pd.read_csv(LE_DATA_PATH,index_col=False, chunksize=chunksize, header=None, sep="\t"):
        
        cols = [2,3,4]
        chunk.drop(chunk.columns[cols],axis=1,inplace=True)
        chunk.columns = ["user_id","artist_id"]
        
        topArtists_helper = chunk[chunk['user_id'].isin(b6_17)]
        top_artists_b6_17 = top_artists_b6_17.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(b18_21)]
        top_artists_b18_21 = top_artists_b18_21.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(b22_25)]
        top_artists_b22_25 = top_artists_b22_25.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(b26_30)]
        top_artists_b26_30 = top_artists_b26_30.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(b31_40)]
        top_artists_b31_40 = top_artists_b31_40.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(b41_50)]
        top_artists_b41_50 = top_artists_b41_50.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(b51_60)]
        top_artists_b51_60 = top_artists_b51_60.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(b61_100)]
        top_artists_b61_100 = top_artists_b61_100.append(topArtists_helper)
        
    fin1 = pd.DataFrame(top_artists_b6_17['artist_id'].value_counts())
    fin2 = pd.DataFrame(top_artists_b18_21['artist_id'].value_counts())
    fin3 = pd.DataFrame(top_artists_b22_25['artist_id'].value_counts())
    fin4 = pd.DataFrame(top_artists_b26_30['artist_id'].value_counts())
    fin5 = pd.DataFrame(top_artists_b31_40['artist_id'].value_counts())
    fin6 = pd.DataFrame(top_artists_b41_50['artist_id'].value_counts())
    fin7 = pd.DataFrame(top_artists_b51_60['artist_id'].value_counts())
    fin8 = pd.DataFrame(top_artists_b61_100['artist_id'].value_counts())

    fin1.to_csv("top_artists_b6_17.csv", sep='\t')
    fin2.to_csv("top_artists_b18_21.csv", sep='\t')
    fin3.to_csv("top_artists_b22_25.csv", sep='\t')
    fin4.to_csv("top_artists_b26_30.csv", sep='\t')
    fin5.to_csv("top_artists_b31_40.csv", sep='\t')
    fin6.to_csv("top_artists_b41_50.csv", sep='\t')
    fin7.to_csv("top_artists_b51_60.csv", sep='\t')
    fin8.to_csv("top_artists_b61_100.csv", sep='\t')
    
    print("finished!")