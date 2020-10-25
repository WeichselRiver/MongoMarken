#%% Load data
import pymongo
import ssl



db = client.Berlin_West   #Select the database
collect = db.Container1 #Select the collection
saetze = db.Satz #Select the collection


# %% get data
Marken = collect.find()


mn_group = collect.aggregate([
    { "$match" : {"Entwertung" : "o"}},
    { "$group": { "_id": "$MichNr", "total": { "$sum": "$Anzahl" } } },
])

for mn in mn_group:
    print(mn)
 


# %%
saetze.find_one()




# %%

list(Marken.aggregate([
      { "$group": { "_id": "$Gebiet", "total": { "$sum": "$Anzahl" } } },
]))
# %%
list(Marken.aggregate([
      { "$match": { "MichNr": 1}}
]))

# %%
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
from pymongo import MongoClient

client = MongoClient('mongodb+srv://Admin:Feynman314@cluster0.imglv.azure.mongodb.net/test?authSource=admin&replicaSet=atlas-y1poto-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true')
result = client['Briefmarken']['AB Gemeinschaft'].aggregate([
    {
        '$match': {
            'Besitz': -1
        }
    }, {}
])
# %%
