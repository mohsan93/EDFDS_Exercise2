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

##returns a list with the users filtered in nationality bins
##first element of the list contains description of the groups
def get_nationality_bins():
    
    user_subset=read_data()
    
    grouped = user_subset.groupby('country').count().reset_index()
    grouped=grouped.sort_values('user_id', ascending=False).head(25)
    
    countries=grouped["country"].values
    
    ret=[]
    
    ret.append(countries.tolist())
    
    for idx, c in enumerate(countries):
        filtered=user_subset[user_subset['country'].isin([countries[idx]])]
        ret.append(filtered)
    
    return ret
    
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
    
    #user_ids.user_id = user_ids.user_id.astype('int64')
    
    
    
    #print(user_ids)
    
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

    #user_ids = balanced_users[["user_id"]]
    #user_ids.user_id = user_ids.user_id.astype('int64')
        
    #chunksize = 100000
    chunksize=50000
    counter=0
    
    #onlyOneChunk = True
    for chunk in pd.read_csv(LE_DATA_PATH,index_col=False, chunksize=chunksize, header=None, sep="\t"):
        
        #print(chunk)
        #chunk.columns = ["user_id","artist_id","album_id","track-id","timestamp"]
        
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
        
        #onlyOneChunk = False
        #counter=counter+1
        #if counter == 20:
        #    break
        
    #topArtists = topArtists.drop_duplicates()
    fin1 = pd.DataFrame(top_artists_b6_17['artist_id'].value_counts())
    fin2 = pd.DataFrame(top_artists_b18_21['artist_id'].value_counts())
    fin3 = pd.DataFrame(top_artists_b22_25['artist_id'].value_counts())
    fin4 = pd.DataFrame(top_artists_b26_30['artist_id'].value_counts())
    fin5 = pd.DataFrame(top_artists_b31_40['artist_id'].value_counts())
    fin6 = pd.DataFrame(top_artists_b41_50['artist_id'].value_counts())
    fin7 = pd.DataFrame(top_artists_b51_60['artist_id'].value_counts())
    fin8 = pd.DataFrame(top_artists_b61_100['artist_id'].value_counts())
    #fin2.columns = ["counts"]
    #fin2 = fin2.reset_index()
    #fin2 = fin2.rename(index=str, columns={"index": "Artist_id", "counts": "Counts"})
    #print(topArtists)   
    #print(fin2)
    fin1.to_csv("top_artists_b6_17.csv", sep='\t')
    fin2.to_csv("top_artists_b18_21.csv", sep='\t')
    fin3.to_csv("top_artists_b22_25.csv", sep='\t')
    fin4.to_csv("top_artists_b26_30.csv", sep='\t')
    fin5.to_csv("top_artists_b31_40.csv", sep='\t')
    fin6.to_csv("top_artists_b41_50.csv", sep='\t')
    fin7.to_csv("top_artists_b51_60.csv", sep='\t')
    fin8.to_csv("top_artists_b61_100.csv", sep='\t')
    
    print("finished!")
        

    
    