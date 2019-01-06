import pandas as pd

USERS_DATA_PATH='data/LFM-1b_users.txt'

data = pd.read_csv(USERS_DATA_PATH, sep="\t", header=0)

data=data.dropna(subset=['country',"gender","age"])
data=data[data.age != -1]
#data=data[data.age > 18]
#data=data[data.age < 100]
data=data[data.playcount >= 500]
data=data[data.gender != "n"]

print("Number of users: " + str(len(data.index)))

#print(data.country.unique())
#print(data.age.unique())
#print(data.gender.unique())





