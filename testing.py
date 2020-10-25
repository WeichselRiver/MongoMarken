#%% 
from pymongo import MongoClient
client = MongoClient('localhost', 27017)


# %%
Marken = client.Briefmarken.Berlin_West


# %%
print(Marken.find_one())

# %%
from datetime import datetime
print(Marken.find_one())
ins = {'MichNr': 10, 
'Gebiet': 'Berlin West',
 'Album': 5,
  'Entwertung': '**',
   'Anzahl': 0,
   'InsTime' : datetime.now(),
   'Variante' : [
       { 'Farbe' : 'a'},
       { 'Rand' : 'linke obere Ecke'}
   ]}
post_id = Marken.insert_one(ins)


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
