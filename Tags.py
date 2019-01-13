# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:53:04 2019

@author: kinde
"""

import numpy as np
import pandas as pd


#WORKING CODE::

'''


#get all artists IDs in the training set:
frame = pd.read_csv("userArtistMatrix\mergedUserArtist.csv", sep="\t")
frame = frame.drop(frame.columns[0], axis=1)
frame = frame.drop_duplicates()
artists = frame[['artist_id']].drop_duplicates()
artistIdList = artists['artist_id'].tolist()
print("artistIDList size: ", len(artistIdList))

#getting their names:
artistNames = pd.read_csv("LFM-1b_artists.txt", sep="\t", header=None)
artistNames.columns = ['artist_id', 'artist_name']
artistNames = artistNames[artistNames['artist_id'].isin(artistIdList)].drop_duplicates()
artistNameList = artistNames['artist_name'].tolist()

#find their tags:
#a) loading the artist names from that weird tag file:

import csv
ArtistTagList = [[]]

with open('artistId_tags_filtered.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    once = True
    for row in csv_reader:
            row = row[1:]
            diff = 201 - len(row)
            for i in range(0,diff):
                row.append(np.NaN)
            ArtistTagList.append(row)


#create column names:
col_names =[]
for i in range(0,201):
    col_names.append("COL_" + str(i))
    
#from that dataframe, filter out the artists that do not belong to our training set per name
ArtistTagDF = pd.DataFrame(ArtistTagList, columns = col_names)

#merging the ArtistTagDF with

#tags = pd.DataFrame(columns=col_names)

ArtistTagDF = ArtistTagDF[ArtistTagDF['COL_0'].isin(artistNameList)]
print(ArtistTagDF.head(),ArtistTagDF.shape)

#now i need to count the tags
tagsOnly = []
for j in range (1,200,2):
    col = "COL_" + str(j)
    tagsOnly= ArtistTagDF[col].tolist()
    tagsOnlyDF = pd.DataFrame(data = tagsOnly)
    tagsOnlyDFCount = tagsOnlyDF[tagsOnlyDF.columns[0]].value_counts()
    tagsOnlyDFCount.to_csv(col + ".csv")

    
'''
#groupby check:
'''
d = {'col1': [1, 1, 2], 'col2': [1, 2, 3]}
df = pd.DataFrame(data=d)
print(df)
print()
print(df.groupby([df.columns[0]]).sum())
print(df.columns)
'''

#merge the multiple files into one:
import glob

path =r'top5000tags' # use your path
allFiles = glob.glob(path + "/*.csv")

list_ = []

for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=None, sep='\t')
    list_.append(df)

frame = pd.concat(list_)
frameFin = frame.groupby([frame.columns[0]]).sum()
frameFin.reset_index(inplace=True)
print(frameFin.head())
frameFin = frameFin.sort_values(by=[frameFin.columns[1]], ascending=False)
frameFin.columns = ['Tag','count']
print(frameFin.head())

frameFin[:5000].to_csv("top5000Tags.csv")


