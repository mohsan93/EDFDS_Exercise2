# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:29:05 2019

@author: kinde
"""

import numpy as np
import pandas as pd



frame = pd.read_csv("userArtistMatrix\mergedUserArtist.csv", sep="\t")
frame = frame.drop(frame.columns[0], axis=1)
frame = frame.drop_duplicates()
frame = frame.loc[frame['gender'] == "m"]
users = frame[['user_id']].drop_duplicates()
users[:2545]['user_id'].to_csv("2545MaleUsers.csv", sep='\t')
userlist = users[:2545]['user_id'].tolist()

LEsubset = frame[frame['user_id'].isin(userlist)]


femaleArtists = pd.read_csv("top5000FemaleArtists.csv", sep="\t")
AllArtists = pd.read_csv("top5000ArtistsCompleteUserBase.csv", sep="\t")

femaleArtists = femaleArtists.drop(femaleArtists.columns[0], axis=1)
AllArtists = AllArtists.drop(AllArtists.columns[0], axis=1)


femaleArtistList = femaleArtists['artist_id'].tolist()
AllArtistsList = AllArtists['artist_id'].tolist()


LEsubset_artists = LEsubset[~LEsubset['artist_id'].isin(femaleArtistList)]
LEsubset_artists = LEsubset[~LEsubset['artist_id'].isin(AllArtistsList)]

LEsubset_artists_count = LEsubset_artists['artist_id'].value_counts()
LEsubset_artists_count = LEsubset_artists_count.reset_index()
LEsubset_artists_count.columns = ['artist_id', 'count']

print(LEsubset_artists_count.head())
print(LEsubset_artists.head())
LEsubset_artists_count[:5000].to_csv("top5000MaleArtists.csv", sep='\t')