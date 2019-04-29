import pymongo
from pymongo import MongoClient
from pprint import pprint

#--------------read the dataset--------------

single_data={"latitude":0,
             "longitude":0,
             "datetime":0,
             "confidence":0,
             "date":0,
             "surface_temperature_celcius":0}

entire_data=[]

data=open("hotspot_historic.csv","r")
next(data) # skip first line

for line in data:
    data_list = line.strip().split(",")
    single_data["latitude"]=float(data_list[0])
    single_data["longitude"]=float(data_list[1])
    single_data["datetime"]=data_list[2]
    single_data["confidence"]=int(data_list[3])
    single_data["date"]=data_list[4]
    single_data["surface_temperature_celcius"]=int(data_list[5])
    entire_data.append(single_data.copy())

print(entire_data)

#-------------load the dataset to mongoDB----------

client=MongoClient("localhost",9999)
db=client.fit5148_assignment
db.hotspot_historic.drop()
hotspot_historic=db.hotspot_historic
hotspot_historic.insert_many(entire_data)
result=hotspot_historic.find()
for document in result:
    pprint(document)