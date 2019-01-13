#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 19:42:47 2019

@author: sztkp
"""

import pandas as pd

a6_17=pd.read_csv("RAW_top_artists_b6_17.csv", sep="\t", header=0)
a6_17.columns=["artist_id","count"]
a6_17=a6_17.head(5000)
a6_17.to_csv("top_artists_b6_17.csv", sep='\t')

a18_21=pd.read_csv("RAW_top_artists_b18_21.csv", sep="\t", header=0)
a18_21.columns=["artist_id","count"]
a18_21=a18_21.head(5000)
a18_21.to_csv("top_artists_b18_21.csv", sep='\t')

a22_25=pd.read_csv("RAW_top_artists_b22_25.csv", sep="\t", header=0)
a22_25.columns=["artist_id","count"]
a22_25=a22_25.head(5000)
a22_25.to_csv("top_artists_b22_25.csv", sep='\t')

a26_30=pd.read_csv("RAW_top_artists_b26_30.csv", sep="\t", header=0)
a26_30.columns=["artist_id","count"]
a26_30=a26_30.head(5000)
a26_30.to_csv("top_artists_b26_30.csv", sep='\t')

a31_40=pd.read_csv("RAW_top_artists_b31_40.csv", sep="\t", header=0)
a31_40.columns=["artist_id","count"]
a31_40=a31_40.head(5000)
a31_40.to_csv("top_artists_b31_40.csv", sep='\t')

a41_50=pd.read_csv("RAW_top_artists_b41_50.csv", sep="\t", header=0)
a41_50.columns=["artist_id","count"]
a41_50=a41_50.head(5000)
a41_50.to_csv("top_artists_b41_50.csv", sep='\t')

a51_60=pd.read_csv("RAW_top_artists_b51_60.csv", sep="\t", header=0)
a51_60.columns=["artist_id","count"]
a51_60=a51_60.head(5000)
a51_60.to_csv("top_artists_b51_60.csv", sep='\t')

a61_100=pd.read_csv("RAW_top_artists_b61_100.csv", sep="\t", header=0)
a61_100.columns=["artist_id","count"]
a61_100=a61_100.head(5000)
a61_100.to_csv("top_artists_b61_100.csv", sep='\t')