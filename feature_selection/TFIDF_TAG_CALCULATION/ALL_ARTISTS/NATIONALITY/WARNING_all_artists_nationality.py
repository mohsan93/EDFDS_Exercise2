#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 19:16:29 2019

@author: sztkp
"""

import numpy as np
import pandas as pd
import os


USERS_FILTER_PATH='../data/LFM-1b_subset_MTAP2018.csv'


def is_non_zero_file(fpath):  
    return True if os.path.isfile(fpath) and os.path.getsize(fpath) > 0 else False

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
    
def process_chunk(chunk_path,chunk_nr,country_bins):
    
    print("PROCESSING CHUNK NR. " + str(chunk_nr))
    
    #country_names=country_bins[0]
    
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
    
    for chunk in pd.read_csv(chunk_path,index_col=False, chunksize=chunksize, header=None, sep="\t"):
        #chunk.columns = ["user_id","artist_id","album_id","track-id","timestamp"]      
        cols = [0,2,3,4,6,7,8]
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
    
    print("data output! for chunk " + str(chunk_nr))
    
    #### RANK 1-10 ###
        
    top_artists_c1.drop(['user_id'], axis=1, inplace=True)
    top_artists_c1.drop_duplicates(inplace=True)
    top_artists_c1.to_csv("rank1_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c2.drop(['user_id'], axis=1, inplace=True)
    top_artists_c2.drop_duplicates(inplace=True)
    top_artists_c2.to_csv("rank2_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c3.drop(['user_id'], axis=1, inplace=True)
    top_artists_c3.drop_duplicates(inplace=True)
    top_artists_c3.to_csv("rank3_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c4.drop(['user_id'], axis=1, inplace=True)
    top_artists_c4.drop_duplicates(inplace=True)
    top_artists_c4.to_csv("rank4_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c5.drop(['user_id'], axis=1, inplace=True)
    top_artists_c5.drop_duplicates(inplace=True)
    top_artists_c5.to_csv("rank5_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c6.drop(['user_id'], axis=1, inplace=True)
    top_artists_c6.drop_duplicates(inplace=True)
    top_artists_c6.to_csv("rank6_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c7.drop(['user_id'], axis=1, inplace=True)
    top_artists_c7.drop_duplicates(inplace=True)
    top_artists_c7.to_csv("rank7_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c8.drop(['user_id'], axis=1, inplace=True)
    top_artists_c8.drop_duplicates(inplace=True)
    top_artists_c8.to_csv("rank8_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c9.drop(['user_id'], axis=1, inplace=True)
    top_artists_c9.drop_duplicates(inplace=True)
    top_artists_c9.to_csv("rank9_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c10.drop(['user_id'], axis=1, inplace=True)
    top_artists_c10.drop_duplicates(inplace=True)
    top_artists_c10.to_csv("rank10_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    
    
    # #### RANK 11-20 ###
    
    top_artists_c11.drop(['user_id'], axis=1, inplace=True)
    top_artists_c11.drop_duplicates(inplace=True)
    top_artists_c11.to_csv("rank11_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c12.drop(['user_id'], axis=1, inplace=True)
    top_artists_c12.drop_duplicates(inplace=True)
    top_artists_c12.to_csv("rank12_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c13.drop(['user_id'], axis=1, inplace=True)
    top_artists_c13.drop_duplicates(inplace=True)
    top_artists_c13.to_csv("rank13_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c14.drop(['user_id'], axis=1, inplace=True)
    top_artists_c14.drop_duplicates(inplace=True)
    top_artists_c14.to_csv("rank14_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c15.drop(['user_id'], axis=1, inplace=True)
    top_artists_c15.drop_duplicates(inplace=True)
    top_artists_c15.to_csv("rank15_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c16.drop(['user_id'], axis=1, inplace=True)
    top_artists_c16.drop_duplicates(inplace=True)
    top_artists_c16.to_csv("rank16_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c17.drop(['user_id'], axis=1, inplace=True)
    top_artists_c17.drop_duplicates(inplace=True)
    top_artists_c17.to_csv("rank17_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c18.drop(['user_id'], axis=1, inplace=True)
    top_artists_c18.drop_duplicates(inplace=True)
    top_artists_c18.to_csv("rank18_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c19.drop(['user_id'], axis=1, inplace=True)
    top_artists_c19.drop_duplicates(inplace=True)
    top_artists_c19.to_csv("rank19_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c20.drop(['user_id'], axis=1, inplace=True)
    top_artists_c20.drop_duplicates(inplace=True)
    top_artists_c20.to_csv("rank20_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    
    
    # #### RANK 21-25 ###
    
    top_artists_c21.drop(['user_id'], axis=1, inplace=True)
    top_artists_c21.drop_duplicates(inplace=True)
    top_artists_c21.to_csv("rank21_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c22.drop(['user_id'], axis=1, inplace=True)
    top_artists_c22.drop_duplicates(inplace=True)
    top_artists_c22.to_csv("rank22_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c23.drop(['user_id'], axis=1, inplace=True)
    top_artists_c23.drop_duplicates(inplace=True)
    top_artists_c23.to_csv("rank23_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c24.drop(['user_id'], axis=1, inplace=True)
    top_artists_c24.drop_duplicates(inplace=True)
    top_artists_c24.to_csv("rank24_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    top_artists_c25.drop(['user_id'], axis=1, inplace=True)
    top_artists_c25.drop_duplicates(inplace=True)
    top_artists_c25.to_csv("rank25_" + "all_artists_chunk." + str(chunk_nr), sep='\n',index=False,header=False)
    
    
        
    print("finished with chunk: " + str(chunk_nr)) 
    
def combine_chunks():
    
    for x in range(1, 26):
        print("X:" + str(x))
        i=1
        temp=pd.DataFrame()
        
        while i<=109:
            f_name="rank" +str(x)+ "_all_artists_chunk." + str(i)
            
            if is_non_zero_file(f_name):
                f_data=pd.read_csv(f_name,index_col=False, header=None, sep="\n")
                temp = temp.append(f_data)
            
            i=i+1
            
        temp.drop_duplicates(inplace=True)
        temp.to_csv(("A_rank" +str(x)+ "_all_artists.COMPLETE"), sep='\n',index=False,header=False)


if __name__ == '__main__':

    country_bins=get_nationality_bins()

    i=1
    
    while i<=109:
        chunk_path="../data/filtered_LE/LFM-1b_LEs_subset" +str(i) +".csv"
        process_chunk(chunk_path,i,country_bins)
        i=i+1
        
    combine_chunks()

