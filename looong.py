# Computes several statistics and provides some tools for the LFM-1b dataset of Last.fm listening histories.
# Author: Markus Schedl

import numpy as np
import h5py
from scipy import sparse
import pandas as pd

UAM_MATLAB_FILE = 'data/LFM-1b_LEs.mat'                  # Matlab .mat file where the listening events are stored
STATISTICS_OUTPUT_FILE = 'out.txt'         # output file for statistics

# Read the user-artist-matrix and corresponding artist and user indices from Matlab file
def read_UAM(m_file):
    mf = h5py.File(m_file, 'r')
    user_ids = np.array(mf.get('idx_users')).astype(np.int64)
    artist_ids = np.array(mf.get('idx_artists')).astype(np.int64)
    # Load UAM
    UAM = sparse.csr_matrix((mf['/LEs/']["data"],
                             mf['/LEs/']["ir"],
                             mf['/LEs/']["jc"])).transpose()    #.tocoo().transpose()
    # user and artist indices to access UAM
    UAM_user_idx = UAM.indices #UAM.row -> for COO matrix
    UAM_artist_idx = UAM.indptr #UAM.col -> for COO matrix
    return UAM, UAM_user_idx, UAM_artist_idx, user_ids, artist_ids



# Main program
if __name__ == '__main__':
    
    #############PREPARING FILTERED USERS LIST
    
    USERS_DATA_PATH='data/LFM-1b_users.txt'

    f_users = pd.read_csv(USERS_DATA_PATH, sep="\t", header=0)

    f_users=f_users.dropna(subset=['country',"gender","age"])
    f_users=f_users[f_users.age > 3] ######sensible?
    f_users=f_users[f_users.gender != "n"]
    
    f_users=f_users["user_id"].values
    
    ###########################################
    
    # Read UAM
    UAM, UAM_user_idx, UAM_artist_idx, user_ids, artist_ids = read_UAM(UAM_MATLAB_FILE)
    print('Users: ', len(user_ids))
    print('Artists: ', len(artist_ids))
    
    found=[]

    # Compute some basic statistics
    pc_sum = np.zeros((len(user_ids)), dtype=np.int32)              # to hold sum of playcounts, for all users
         # to hold standard deviation of playcount per artist, for all users
    for i in range(0, len(user_ids)):
        
        if user_ids[i] in f_users:
            pc_i = UAM.getrow(i).toarray()                    # get playcount vector for user i
            idx_nz = np.nonzero(pc_i)                         # indies of non-zero playcounts
            pc_sum[i] = np.sum(pc_i[idx_nz])
           
            #print('User ' + str(i) +    "   Playcount: " + str(pc_sum[i]))
            #print("USER ID: " + str(user_ids[i]))
            
            print("Progress: " +     str(  (     (     (i+1)/(len(user_ids))  )  )   ) + "%" )
            
            if user_ids[i] in f_users and pc_sum[i] >= 500: #check if current id is among filtered users and if the current user has a playcount higher that 500
                found.append(str(user_ids[i]))
            
            print(" ")
    # Store to file
    with open(STATISTICS_OUTPUT_FILE, 'w') as f:
        for item in found:
            f.write("%s\n" % item)

    # Mean/std. of basic statistics
    #print("Mean/std. of playcount: " + str(np.mean(pc_sum)) + " +- " + str(np.std(pc_sum)))
    #print("Mean/std. of unique artists: " + str(np.mean(pc_uniq_artists)) + " +- " + str(np.std(pc_uniq_artists)))
    #print("Mean/std. of mean PC/artist: " + str(np.mean(pc_mean)) + " +- " + str(np.std(pc_mean)))
    #print("Mean/std. of std. PC/artist: " + str(np.mean(pc_std)) + " +- " + str(np.std(pc_std)))
    #print("Mean/std. of median PC/artist: " + str(np.mean(pc_median)) + " +- " + str(np.std(pc_median)))
