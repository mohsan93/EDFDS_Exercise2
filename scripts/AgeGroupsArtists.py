# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:29:05 2019

@author: kinde
"""

import numpy as np
import pandas as pd

#groups: [6–17], [18–21], [22–25], [26–30], [31–40], [41–50],[51–60], and [61–100].


AllUsers = pd.read_csv("mergedUserArtist.csv", sep="\t")
AllUsers = AllUsers.drop(AllUsers.columns[0], axis=1)
AllUsers = AllUsers.drop_duplicates()

top5000artists = pd.read_csv("top5000ArtistsCompleteUserBase.csv", sep="\t")
top5000artists = top5000artists.drop(top5000artists.columns[0], axis=1)
top5000artistslist = top5000artists['artist_id'].tolist()



Age1 = AllUsers.loc[(AllUsers['age'] >= 6) & (AllUsers['age'] <=17)]
Age2 = AllUsers.loc[(AllUsers['age'] >= 18) & (AllUsers['age'] <=21)]
Age3 = AllUsers.loc[(AllUsers['age'] >= 22) & (AllUsers['age'] <=25)]
Age4 = AllUsers.loc[(AllUsers['age'] >= 26) & (AllUsers['age'] <=30)]
Age5 = AllUsers.loc[(AllUsers['age'] >= 31) & (AllUsers['age'] <=40)]
Age6 = AllUsers.loc[(AllUsers['age'] >= 41) & (AllUsers['age'] <=50)]
Age7 = AllUsers.loc[(AllUsers['age'] >= 51) & (AllUsers['age'] <=60)]
Age8 = AllUsers.loc[(AllUsers['age'] >= 61) & (AllUsers['age'] <=100)]

TopArtistAge1 = Age1['artist_id'].value_counts()
TopArtistAge1 = TopArtistAge1.reset_index()
TopArtistAge1.columns = ['artist_id', 'count']

TopArtistAge2= Age2['artist_id'].value_counts()
TopArtistAge2 = TopArtistAge2.reset_index()
TopArtistAge2.columns = ['artist_id', 'count']

TopArtistAge3 = Age3['artist_id'].value_counts()
TopArtistAge3 = TopArtistAge3.reset_index()
TopArtistAge3.columns = ['artist_id', 'count']

TopArtistAge4 = Age4['artist_id'].value_counts()
TopArtistAge4 = TopArtistAge4.reset_index()
TopArtistAge4.columns = ['artist_id', 'count']

TopArtistAge5 = Age5['artist_id'].value_counts()
TopArtistAge5 = TopArtistAge5.reset_index()
TopArtistAge5.columns = ['artist_id', 'count']

TopArtistAge6 = Age6['artist_id'].value_counts()
TopArtistAge6 = TopArtistAge6.reset_index()
TopArtistAge6.columns = ['artist_id', 'count']

TopArtistAge7 = Age7['artist_id'].value_counts()
TopArtistAge7 = TopArtistAge7.reset_index()
TopArtistAge7.columns = ['artist_id', 'count']

TopArtistAge8 = Age8['artist_id'].value_counts()
TopArtistAge8 = TopArtistAge8.reset_index()
TopArtistAge8.columns = ['artist_id', 'count']


top5000artists = pd.read_csv("top5000ArtistsCompleteUserBase.csv", sep="\t")
top5000artists = top5000artists.drop(top5000artists.columns[0], axis=1)
top5000artistslist = top5000artists['artist_id'].tolist()

TopArtistAge1 = TopArtistAge1[~TopArtistAge1['artist_id'].isin(top5000artistslist)]

TopArtistAge1[:625].to_csv("TopArtistAge1.csv", sep="\t", index = False)


TopArtistAge1List = TopArtistAge1[:625]['artist_id'].tolist()

TopArtistAge2 = TopArtistAge2[~TopArtistAge2['artist_id'].isin(top5000artistslist)]
TopArtistAge2 = TopArtistAge2[~TopArtistAge2['artist_id'].isin(TopArtistAge1List)]
TopArtistAge2[:625].to_csv("TopArtistAge2.csv", sep="\t", index = False)
TopArtistAge2List = TopArtistAge2[:625]['artist_id'].tolist()

TopArtistAge3 = TopArtistAge3[~TopArtistAge3['artist_id'].isin(top5000artistslist)]
TopArtistAge3 = TopArtistAge3[~TopArtistAge3['artist_id'].isin(TopArtistAge1List)]
TopArtistAge3 = TopArtistAge3[~TopArtistAge3['artist_id'].isin(TopArtistAge2List)]
TopArtistAge3[:625].to_csv("TopArtistAge3.csv", sep="\t", index = False)
TopArtistAge3List = TopArtistAge3[:625]['artist_id'].tolist()


TopArtistAge4 = TopArtistAge4[~TopArtistAge4['artist_id'].isin(top5000artistslist)]
TopArtistAge4 = TopArtistAge4[~TopArtistAge4['artist_id'].isin(TopArtistAge1List)]
TopArtistAge4 = TopArtistAge4[~TopArtistAge4['artist_id'].isin(TopArtistAge2List)]
TopArtistAge4 = TopArtistAge4[~TopArtistAge4['artist_id'].isin(TopArtistAge3List)]
TopArtistAge4[:625].to_csv("TopArtistAge4.csv", sep="\t", index = False)
TopArtistAge4List = TopArtistAge4[:625]['artist_id'].tolist()


TopArtistAge5 = TopArtistAge5[~TopArtistAge5['artist_id'].isin(top5000artistslist)]
TopArtistAge5 = TopArtistAge5[~TopArtistAge5['artist_id'].isin(TopArtistAge1List)]
TopArtistAge5 = TopArtistAge5[~TopArtistAge5['artist_id'].isin(TopArtistAge2List)]
TopArtistAge5 = TopArtistAge5[~TopArtistAge5['artist_id'].isin(TopArtistAge3List)]
TopArtistAge5 = TopArtistAge5[~TopArtistAge5['artist_id'].isin(TopArtistAge4List)]
TopArtistAge5[:625].to_csv("TopArtistAge5.csv", sep="\t", index = False)
TopArtistAge5List = TopArtistAge5[:625]['artist_id'].tolist()

TopArtistAge6 = TopArtistAge6[~TopArtistAge6['artist_id'].isin(top5000artistslist)]
TopArtistAge6 = TopArtistAge6[~TopArtistAge6['artist_id'].isin(TopArtistAge1List)]
TopArtistAge6 = TopArtistAge6[~TopArtistAge6['artist_id'].isin(TopArtistAge2List)]
TopArtistAge6 = TopArtistAge6[~TopArtistAge6['artist_id'].isin(TopArtistAge3List)]
TopArtistAge6 = TopArtistAge6[~TopArtistAge6['artist_id'].isin(TopArtistAge4List)]
TopArtistAge6 = TopArtistAge6[~TopArtistAge6['artist_id'].isin(TopArtistAge5List)]
TopArtistAge6[:625].to_csv("TopArtistAge6.csv", sep="\t", index = False)
TopArtistAge6List = TopArtistAge6[:625]['artist_id'].tolist()


TopArtistAge7 = TopArtistAge7[~TopArtistAge7['artist_id'].isin(top5000artistslist)]
TopArtistAge7 = TopArtistAge7[~TopArtistAge7['artist_id'].isin(TopArtistAge1List)]
TopArtistAge7 = TopArtistAge7[~TopArtistAge7['artist_id'].isin(TopArtistAge2List)]
TopArtistAge7 = TopArtistAge7[~TopArtistAge7['artist_id'].isin(TopArtistAge3List)]
TopArtistAge7 = TopArtistAge7[~TopArtistAge7['artist_id'].isin(TopArtistAge4List)]
TopArtistAge7 = TopArtistAge7[~TopArtistAge7['artist_id'].isin(TopArtistAge5List)]
TopArtistAge7 = TopArtistAge7[~TopArtistAge7['artist_id'].isin(TopArtistAge6List)]
TopArtistAge7[:625].to_csv("TopArtistAge7.csv", sep="\t", index = False)
TopArtistAge7List = TopArtistAge7[:625]['artist_id'].tolist()


TopArtistAge8 = TopArtistAge8[~TopArtistAge8['artist_id'].isin(top5000artistslist)]
TopArtistAge8 = TopArtistAge8[~TopArtistAge8['artist_id'].isin(TopArtistAge1List)]
TopArtistAge8 = TopArtistAge8[~TopArtistAge8['artist_id'].isin(TopArtistAge2List)]
TopArtistAge8 = TopArtistAge8[~TopArtistAge8['artist_id'].isin(TopArtistAge3List)]
TopArtistAge8 = TopArtistAge8[~TopArtistAge8['artist_id'].isin(TopArtistAge4List)]
TopArtistAge8 = TopArtistAge8[~TopArtistAge8['artist_id'].isin(TopArtistAge5List)]
TopArtistAge8 = TopArtistAge8[~TopArtistAge8['artist_id'].isin(TopArtistAge6List)]
TopArtistAge8 = TopArtistAge8[~TopArtistAge8['artist_id'].isin(TopArtistAge7List)]
TopArtistAge8[:625].to_csv("TopArtistAge8.csv", sep="\t", index = False)
TopArtistAge8List = TopArtistAge8[:625]['artist_id'].tolist()


#LEsubset_artists = LEsubset[~LEsubset['artist_id'].isin(femaleArtistList)]
