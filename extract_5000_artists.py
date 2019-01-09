# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:55:13 2019

@author: kinde
"""

import numpy as np
import pandas as pd

############# REMOVE USERS WITH MISSING DEMOGHRAPHIC DATA #############

USERS_DATA_PATH='LFM-1b_subset_MTAP2018.csv'

f_users = pd.read_csv(USERS_DATA_PATH, sep="\t", header=None)
f_users.columns = ["user_id", "age", "gender", "country"]
f_users = f_users.iloc[1:]
f_users = pd.DataFrame(data=f_users)



#there are 2545 females in the dataset, now ill choose 2545 males and combine the male and female dataset, and then shuffle it

#shuffle the dataframe before extracing the males:
f_users = f_users.sample(frac=1).reset_index(drop=True)

#create female only dataframe:
females = f_users.loc[f_users['gender'] == "f"]

#create male-only Dataframe with the exact size of the female dataframe
males= f_users.loc[f_users['gender'] == "m"][:2545]

#creating the balnaced Dataframe by merging the male and the female one
balanced_users =  pd.concat([females,males])

#shuffling the balanced dataset
balanced_users = balanced_users.sample(frac=1).reset_index(drop=True)


#reading in the big file LFM-1b_LEs.txt, COLUMNS: User-id, artist-id, album-id, track-id, timestamp --------------------------------
#Task: find the 5000 most listened to artists (of the balanced_users)

#exctracting the user IDs only from the balanced dataset for simplicity:
user_ids = balanced_users[["user_id"]]
user_ids.user_id = user_ids.user_id.astype('int64')

topArtists_helper = pd.DataFrame() #Empty dataframe to store the users with their corresponding playcount
topArtists = pd.DataFrame()

#Read the 'LFM-1b_LEs.txt' in chunks of 10 Millions.
#The data is grouped based on the users ids and the number of listening event is counted for each user. 
chunksize = 100000
#file columns: User-id, artist-id, album-id, track-id, timestamp


onlyOneChunk = False
for chunk in pd.read_csv('LFM-1b_LEs.txt',index_col=False, chunksize=chunksize, header=None, sep="\t"):
    if onlyOneChunk == True:
        break
    chunk.columns = ["user_id","artist_id","album_id","track-id","timestamp"]
    topArtists_helper = pd.merge(user_ids, chunk, on="user_id")[["user_id","artist_id"]].drop_duplicates()
    topArtists = topArtists.append(topArtists_helper)
    onlyOneChunk = False
    
topArtists.to_csv("top_artists_", sep='\t')
print("finished!")

#todo: drop dupllicates, drop user id, count columns, sort


'''
#experiments/testing pandas dataframe funcitons to extract the 5000 most listened to users in the training set of our users:

d = {'userID': [1, 5,5,3], 'artist-id': [3, 4,4,4]}
df_user_artist = pd.DataFrame(data=d)

d = {'userID': [1, 5 , 3]}
df_users = pd.DataFrame(data=d)
#User-id, artist-id, album-id, track-id, timestamp
fin = pd.merge(df_users, df_user_artist, on="userID").drop_duplicates()
fin2 = pd.DataFrame(fin['artist-id'].value_counts())
fin2.columns = ["counts"]
fin2 = fin2.reset_index()
fin2 = fin2.rename(index=str, columns={"index": "Artist_id", "counts": "Counts"})

print(fin2)
'''