#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 19:16:29 2019

@author: sztkp
"""

import numpy as np
import pandas as pd


USERS_DATA_PATH='data/LFM-1b_users.txt'
USERS_FILTER_PATH='data/LFM-1b_subset_MTAP2018.csv'


def read_data():
    user_subset =pd.read_csv(USERS_FILTER_PATH, sep="\t", header=0)
    
    return user_subset

##returns a list with the users filtered in age bins
##first element of the list contains description of the groups
def return_age_bins():
    
    user_subset=read_data();
    
    bins=["6-17","18-21","22-25","26-30","31-40","41-50","51-60","61-100"]
    
    b6_17=user_subset[user_subset['country'].isin(range(6,18))]
    b18_21=user_subset[user_subset['country'].isin(range(18,22))]
    b22_25=user_subset[user_subset['country'].isin(range(22,26))]
    b26_30=user_subset[user_subset['country'].isin(range(26,31))]
    b31_40=user_subset[user_subset['country'].isin(range(31,41))]
    b41_50=user_subset[user_subset['country'].isin(range(41,51))]
    b51_60=user_subset[user_subset['country'].isin(range(51,61))]
    b61_100=user_subset[user_subset['country'].isin(range(61,101))]
    
    return [bins,b6_17,b18_21,b22_25,b26_30,b31_40,b41_50,b51_60,b61_100]

##returns a list with the users filtered in nationality bins
##first element of the list contains description of the groups
def return_nationality_bins():
    
    user_subset=read_data()
    
    grouped = user_subset.groupby('gender').count().reset_index()
    grouped=grouped.sort_values('user_id', ascending=False).head(25)
    
    countries=grouped["gender"].values
    
    ret=[]
    
    ret.append(countries.tolist())
    
    for idx, c in enumerate(countries):
        filtered=user_subset[user_subset['gender'].isin([countries[idx]])]
        ret.append(filtered)
    
    
    return ret
    
if __name__ == '__main__':
    
    age=return_age_bins()
    
    nat=return_nationality_bins()
    