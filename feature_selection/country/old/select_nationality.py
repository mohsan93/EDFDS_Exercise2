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
    
    country_bins=get_nationality_bins()
    country_names=country_bins[0]
    
    ###################################################
    ###GETTING USERS LIST FOR EACH COUNTRY
    
    c_1=country_bins[1]["user_id"].tolist()
    c_2=country_bins[2]["user_id"].tolist()
    c_3=country_bins[3]["user_id"].tolist()
    c_4=country_bins[4]["user_id"].tolist()
    c_5=country_bins[5]["user_id"].tolist()
    c_6=country_bins[6]["user_id"].tolist()
    c_7=country_bins[7]["user_id"].tolist()
    c_8=country_bins[8]["user_id"].tolist()
    c_9=country_bins[9]["user_id"].tolist()
    c_10=country_bins[10]["user_id"].tolist()
    c_11=country_bins[11]["user_id"].tolist()
    c_12=country_bins[12]["user_id"].tolist()
    c_13=country_bins[13]["user_id"].tolist()
    c_14=country_bins[14]["user_id"].tolist()
    c_15=country_bins[15]["user_id"].tolist()
    c_16=country_bins[16]["user_id"].tolist()
    c_17=country_bins[17]["user_id"].tolist()
    c_18=country_bins[18]["user_id"].tolist()
    c_19=country_bins[19]["user_id"].tolist()
    c_20=country_bins[20]["user_id"].tolist()
    c_21=country_bins[21]["user_id"].tolist()
    c_22=country_bins[22]["user_id"].tolist()
    c_23=country_bins[23]["user_id"].tolist()
    c_24=country_bins[24]["user_id"].tolist()
    c_25=country_bins[25]["user_id"].tolist()
        
    ######################################################
    ###PREPARING FRAMES FOR PROCESSING
    
    top_artists_c1=pd.DataFrame()
    top_artists_c2=pd.DataFrame()
    top_artists_c3=pd.DataFrame()
    top_artists_c4=pd.DataFrame()
    top_artists_c5=pd.DataFrame()
    top_artists_c6=pd.DataFrame()
    top_artists_c7=pd.DataFrame()
    top_artists_c8=pd.DataFrame()
    top_artists_c9=pd.DataFrame()
    top_artists_c10=pd.DataFrame()
    top_artists_c11=pd.DataFrame()
    top_artists_c12=pd.DataFrame()
    top_artists_c13=pd.DataFrame()
    top_artists_c14=pd.DataFrame()
    top_artists_c15=pd.DataFrame()
    top_artists_c16=pd.DataFrame()
    top_artists_c17=pd.DataFrame()
    top_artists_c18=pd.DataFrame()
    top_artists_c19=pd.DataFrame()
    top_artists_c20=pd.DataFrame()
    top_artists_c21=pd.DataFrame()
    top_artists_c22=pd.DataFrame()
    top_artists_c23=pd.DataFrame()
    top_artists_c24=pd.DataFrame()
    top_artists_c25=pd.DataFrame()
    
    #######################################################
    ###SETTING UP ARBITRARY VARIABLES
    
    topArtists_helper = pd.DataFrame() 
    chunksize=50000
    #counter=0
    
    #######################################################
    ###TRAVERSING LE FILE AND FILTERING
    
    for chunk in pd.read_csv(LE_DATA_PATH,index_col=False, chunksize=chunksize, header=None, sep="\t"):
        chunk.columns = ["user_id","artist_id","album_id","track-id","timestamp"]      
        cols = [2,3,4]
        chunk.drop(chunk.columns[cols],axis=1,inplace=True)
        chunk.columns = ["user_id","artist_id"]
       
        topArtists_helper = chunk[chunk['user_id'].isin(c_1)]
        top_artists_c1 = top_artists_c1.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_2)]
        top_artists_c2 = top_artists_c2.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_3)]
        top_artists_c3 = top_artists_c3.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_4)]
        top_artists_c4 = top_artists_c4.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_5)]
        top_artists_c5 = top_artists_c5.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_6)]
        top_artists_c6 = top_artists_c6.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_7)]
        top_artists_c7 = top_artists_c7.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_8)]
        top_artists_c8 = top_artists_c8.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_9)]
        top_artists_c9 = top_artists_c9.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_10)]
        top_artists_c10 = top_artists_c10.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_11)]
        top_artists_c11 = top_artists_c11.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_12)]
        top_artists_c12 = top_artists_c12.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_13)]
        top_artists_c13 = top_artists_c13.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_14)]
        top_artists_c14 = top_artists_c14.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_15)]
        top_artists_c15 = top_artists_c15.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_16)]
        top_artists_c16 = top_artists_c16.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_17)]
        top_artists_c17 = top_artists_c17.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_18)]
        top_artists_c18 = top_artists_c18.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_19)]
        top_artists_c19 = top_artists_c19.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_20)]
        top_artists_c20 = top_artists_c20.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_21)]
        top_artists_c21 = top_artists_c21.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_22)]
        top_artists_c22 = top_artists_c22.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_23)]
        top_artists_c23 = top_artists_c23.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_24)]
        top_artists_c24 = top_artists_c24.append(topArtists_helper)
        
        topArtists_helper = chunk[chunk['user_id'].isin(c_25)]
        top_artists_c25 = top_artists_c25.append(topArtists_helper)
        
        
        #counter=counter+1
        
        #if counter==150:
        #    break
        
    #######################################################
    ###COUNTING USER ID-s AND OUTPUTTING FILES
    
    print("data output!")
    
    #### RANK 1-10 ###
        
    fin1 = pd.DataFrame(top_artists_c1['artist_id'].value_counts())
    fin1.reset_index(level=0, inplace=True)
    fin1.columns=["artist_id","count"]
    fin1=fin1.head(5000)
    fin1.to_csv("rank1_" + country_names[0] + "_top_artists.csv", sep='\t')
    
    fin2 = pd.DataFrame(top_artists_c2['artist_id'].value_counts())
    fin2.reset_index(level=0, inplace=True)
    fin2.columns=["artist_id","count"]
    fin2=fin2.head(5000)
    fin2.to_csv("rank2_" + country_names[1] + "_top_artists.csv", sep='\t')
    
    fin3 = pd.DataFrame(top_artists_c3['artist_id'].value_counts())
    fin3.reset_index(level=0, inplace=True)
    fin3.columns=["artist_id","count"]
    fin3=fin3.head(5000)
    fin3.to_csv("rank3_" + country_names[2] + "_top_artists.csv", sep='\t')
    
    fin4 = pd.DataFrame(top_artists_c4['artist_id'].value_counts())
    fin4.reset_index(level=0, inplace=True)
    fin4.columns=["artist_id","count"]
    fin4=fin4.head(5000)
    fin4.to_csv("rank4_" + country_names[3] + "_top_artists.csv", sep='\t')
    
    fin5 = pd.DataFrame(top_artists_c5['artist_id'].value_counts())
    fin5.reset_index(level=0, inplace=True)
    fin5.columns=["artist_id","count"]
    fin5=fin5.head(5000)
    fin5.to_csv("rank5_" + country_names[4] + "_top_artists.csv", sep='\t')
    
    fin6 = pd.DataFrame(top_artists_c6['artist_id'].value_counts())
    fin6.reset_index(level=0, inplace=True)
    fin6.columns=["artist_id","count"]
    fin6=fin6.head(5000)
    fin6.to_csv("rank6_" + country_names[5] + "_top_artists.csv", sep='\t')
    
    fin7 = pd.DataFrame(top_artists_c7['artist_id'].value_counts())
    fin7.reset_index(level=0, inplace=True)
    fin7.columns=["artist_id","count"]
    fin7=fin7.head(5000)
    fin7.to_csv("rank7_" + country_names[6] + "_top_artists.csv", sep='\t')
    
    fin8 = pd.DataFrame(top_artists_c8['artist_id'].value_counts())
    fin8.reset_index(level=0, inplace=True)
    fin8.columns=["artist_id","count"]
    fin8=fin8.head(5000)
    fin8.to_csv("rank8_" + country_names[7] + "_top_artists.csv", sep='\t')
    
    fin9 = pd.DataFrame(top_artists_c9['artist_id'].value_counts())
    fin9.reset_index(level=0, inplace=True)
    fin9.columns=["artist_id","count"]
    fin9=fin9.head(5000)
    fin9.to_csv("rank9_" + country_names[8] + "_top_artists.csv", sep='\t')
    
    fin10 = pd.DataFrame(top_artists_c10['artist_id'].value_counts())
    fin10.reset_index(level=0, inplace=True)
    fin10.columns=["artist_id","count"]
    fin10=fin10.head(5000)
    fin10.to_csv("rank10_" + country_names[9] + "_top_artists.csv", sep='\t')
    
    #### RANK 11-20 ###
    
    fin11 = pd.DataFrame(top_artists_c11['artist_id'].value_counts())
    fin11.reset_index(level=0, inplace=True)
    fin11.columns=["artist_id","count"]
    fin11=fin11.head(5000)
    fin11.to_csv("rank11_" + country_names[10] + "_top_artists.csv", sep='\t')
    
    fin12 = pd.DataFrame(top_artists_c12['artist_id'].value_counts())
    fin12.reset_index(level=0, inplace=True)
    fin12.columns=["artist_id","count"]
    fin12=fin12.head(5000)
    fin12.to_csv("rank12_" + country_names[11] + "_top_artists.csv", sep='\t')
    
    fin13 = pd.DataFrame(top_artists_c13['artist_id'].value_counts())
    fin13.reset_index(level=0, inplace=True)
    fin13.columns=["artist_id","count"]
    fin13=fin13.head(5000)
    fin13.to_csv("rank13_" + country_names[12] + "_top_artists.csv", sep='\t')
    
    fin14 = pd.DataFrame(top_artists_c14['artist_id'].value_counts())
    fin14.reset_index(level=0, inplace=True)
    fin14.columns=["artist_id","count"]
    fin14=fin14.head(5000)
    fin14.to_csv("rank14_" + country_names[13] + "_top_artists.csv", sep='\t')
    
    fin15 = pd.DataFrame(top_artists_c15['artist_id'].value_counts())
    fin15.reset_index(level=0, inplace=True)
    fin15.columns=["artist_id","count"]
    fin15=fin15.head(5000)
    fin15.to_csv("rank15_" + country_names[14] + "_top_artists.csv", sep='\t')
    
    fin16 = pd.DataFrame(top_artists_c16['artist_id'].value_counts())
    fin16.reset_index(level=0, inplace=True)
    fin16.columns=["artist_id","count"]
    fin16=fin16.head(5000)
    fin16.to_csv("rank16_" + country_names[15] + "_top_artists.csv", sep='\t')
    
    fin17 = pd.DataFrame(top_artists_c17['artist_id'].value_counts())
    fin17.reset_index(level=0, inplace=True)
    fin17.columns=["artist_id","count"]
    fin17=fin17.head(5000)
    fin17.to_csv("rank17_" + country_names[16] + "_top_artists.csv", sep='\t')
    
    fin18 = pd.DataFrame(top_artists_c18['artist_id'].value_counts())
    fin18.reset_index(level=0, inplace=True)
    fin18.columns=["artist_id","count"]
    fin18=fin18.head(5000)
    fin18.to_csv("rank18_" + country_names[17] + "_top_artists.csv", sep='\t')
    
    fin19 = pd.DataFrame(top_artists_c19['artist_id'].value_counts())
    fin19.reset_index(level=0, inplace=True)
    fin19.columns=["artist_id","count"]
    fin19=fin19.head(5000)
    fin19.to_csv("rank19_" + country_names[18] + "_top_artists.csv", sep='\t')
    
    fin20 = pd.DataFrame(top_artists_c20['artist_id'].value_counts())
    fin20.reset_index(level=0, inplace=True)
    fin20.columns=["artist_id","count"]
    fin20=fin20.head(5000)
    fin20.to_csv("rank20_" + country_names[19] + "_top_artists.csv", sep='\t')
    
    #### RANK 21-25 ###
    
    fin21 = pd.DataFrame(top_artists_c21['artist_id'].value_counts())
    fin21.reset_index(level=0, inplace=True)
    fin21.columns=["artist_id","count"]
    fin21=fin21.head(5000)
    fin21.to_csv("rank21_" + country_names[20] + "_top_artists.csv", sep='\t')
    
    fin22 = pd.DataFrame(top_artists_c22['artist_id'].value_counts())
    fin22.reset_index(level=0, inplace=True)
    fin22.columns=["artist_id","count"]
    fin22=fin22.head(5000)
    fin22.to_csv("rank22_" + country_names[21] + "_top_artists.csv", sep='\t')
    
    fin23 = pd.DataFrame(top_artists_c23['artist_id'].value_counts())
    fin23.reset_index(level=0, inplace=True)
    fin23.columns=["artist_id","count"]
    fin23=fin23.head(5000)
    fin23.to_csv("rank23_" + country_names[22] + "_top_artists.csv", sep='\t')
    
    fin24 = pd.DataFrame(top_artists_c24['artist_id'].value_counts())
    fin24.reset_index(level=0, inplace=True)
    fin24.columns=["artist_id","count"]
    fin24=fin24.head(5000)
    fin24.to_csv("rank24_" + country_names[23] + "_top_artists.csv", sep='\t')
    
    fin25 = pd.DataFrame(top_artists_c25['artist_id'].value_counts())
    fin25.reset_index(level=0, inplace=True)
    fin25.columns=["artist_id","count"]
    fin25=fin25.head(5000)
    fin25.to_csv("rank25_" + country_names[24] + "_top_artists.csv", sep='\t')
        
    print("finished!")