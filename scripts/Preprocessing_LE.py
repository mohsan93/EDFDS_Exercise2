# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:52:53 2019

@author: User
"""

import numpy as np
import pandas as pd

############# REMOVE USERS WITH MISSING DEMOGHRAPHIC DATA #############

USERS_DATA_PATH='LFM-1b_users.txt'

f_users = pd.read_csv(USERS_DATA_PATH, sep="\t", header=0)
f_users = pd.DataFrame(data=f_users)

f_users=f_users.dropna(subset=['country',"gender","age"])
f_users=f_users[f_users.age   != -1] 
f_users=f_users[f_users.gender != "n"]

f_users_ind=f_users["user_id"].index.values.tolist()


    
############# REMOVE USERS WITH MISSING DEMOGHRAPHIC DATA #############

LE_count = pd.DataFrame() #Empty dataframe to store the users with their corresponding playcount
    

#Read the 'LFM-1b_LEs.txt' in chunks of 10 Millions.
#The data is grouped based on the users ids and the number of listening event is counted for each user. 
chunksize = 10000000
for chunk in pd.read_csv('LFM-1b_LEs.txt',index_col=False, chunksize=chunksize, header=None, sep="\t"):
    LE_count_temp=chunk.groupby(0).count()
    LE_count=LE_count.append(LE_count_temp)
         
    print(str(len(LE_count)))  


LE_count = LE_count.iloc[:,1]
LE_count.columns = ['User','Playcount']
#Since some users appears more than one time in the data, the data should be grouped again based on the users ids and the sum is considered instead of 'count'       
LE_count_final = LE_count.groupby(LE_count.index).sum()
LE_count_final = LE_count_final.to_frame()
LE_count_final.reset_index(level=0, inplace=True)
LE_count_final.columns = ['User','Playcount']
LE_count_final = LE_count_final[LE_count_final.Playcount>=500]
LE_count_final = LE_count_final[LE_count_final['User'].isin(f_users.user_id.tolist())]