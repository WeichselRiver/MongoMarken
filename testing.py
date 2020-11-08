#%% Load data
import pymongo
import ssl
uri = "mongodb://marken:6kwieS9bXJhgqXJL9tvzdl7F4b4s8S37ZssSuhdfb4zQOUzNWYqcRMzPsd4HwxllXlnq1spJJ1J8GAZPoZ69JQ==@marken.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@marken@&retrywrites=false"
client = pymongo.MongoClient(uri, ssl=True)

db = client.Berlin_West   #Select the database
collect = db.Container1 #Select the collection





#%% Delete all documents !!!!

collect.delete_many({})


# %% get data



# mn_group = saetze.aggregate( [ { "$group" : { "_id" : "$Jahrgang" } } ] )

mn_group = saetze.aggregate([
   { "$group" : { "_id" : "$Jahrgang", "Satz": { "$push": ["$Beschreibung", "$MichStart", "$MichEnd"] } } }
 ])

list(mn_group)[0]['Satz'][0][1]

# %%
for mn in mn_group:
    print(mn)
 
#%%
act_set =saetze.find_one()
lb = act_set['MichStart']
ub = act_set['MichEnd']
mn_range = range(lb, ub)

list(collect.find({"MichNr" : {"$in" : list(mn_range)}}))



#%%
mn = 3
set_found = saetze.find_one({"MichStart" : {"$lte": mn}, "MichEnd" : {"$gte": mn}})
list(saetze.find({"_id" : set_found['_id']}))
# %%
