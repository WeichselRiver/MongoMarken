#%% Load data
import pymongo
import ssl
uri = "mongodb://marken:6kwieS9bXJhgqXJL9tvzdl7F4b4s8S37ZssSuhdfb4zQOUzNWYqcRMzPsd4HwxllXlnq1spJJ1J8GAZPoZ69JQ==@marken.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@marken@&retrywrites=false"
client = pymongo.MongoClient(uri, ssl=True)

db = client.Berlin_West   #Select the database
collect = db.Container1 #Select the collection
saetze = db.Satz #Select the collection


# %% get data



# mn_group = saetze.aggregate( [ { "$group" : { "_id" : "$Jahrgang" } } ] )

mn_group = saetze.aggregate([
   { "$group" : { "_id" : "$Jahrgang", "books": { "$push": "$Beschreibung" } } }
 ])

# %%
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
