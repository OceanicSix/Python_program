#In this task, there are two datasets: one is climate data which record climate status per day. The other one is hotspot data in which
# instances of fire in each day are recorded. Therefore, for each record in climate data there could be multiple records in hotspot data
#that contains the data in the same date. Overall, it forms a one-to-many relationship ( climate data is one side whereas hotspot data is the
#many side)

#Given the limited document size in MongoDB and amount of data need to be stored, embedding modeling approach will consume too much
#storage to effieciently store and load from MongoDB. Hence, referercing modelling method is adopted.

#As for how these two dataset are referenced together, the given query which consistute the use case is taken into consideration.Based on
# the query f and g, it is more efficient to have hotspot data keep the "date" field. As a result, the final data model is climate data as
#parent. which is constructed as
# #single_data={"station":0,
#              "date":0,
#              "air_temperature_celcius":0,
#              "relative_humidity":0,
#              "windspeed_knots":0,
#              "max_wind_speed":0,
#              "precipitation":0}


#And it reference its child "hotspot data" through field "date". The hotspot data is constructed as

# single_data={"latitude":0,
#              "longitude":0,
#              "datetime":0,
#              "confidence":0,
#              "date":0,
#              "surface_temperature_celcius":0}

import pymongo
from pymongo import MongoClient
from pprint import pprint

#--------------read the dataset--------------

single_data={"station":0,
             "date":0,
             "air_temperature_celcius":0,
             "relative_humidity":0,
             "windspeed_knots":0,
             "max_wind_speed":0,
             "precipitation":0}

entire_data=[]

data=open("climate_historic.csv","r")
next(data) # skip first line

for line in data:
    data_list = line.strip().split(",")
    single_data["station"]=int(data_list[0])
    single_data["date"]=data_list[1]
    single_data["air_temperature_celcius"]=int(data_list[2])
    single_data["relative_humidity"]=float(data_list[3])
    single_data["windspeed_knots"]=float(data_list[4])
    single_data["max_wind_speed"]=float(data_list[5])
    single_data["precipitation"]=data_list[6]
    entire_data.append(single_data.copy())

pprint(entire_data)


#-------------load the dataset to mongoDB----------

client=MongoClient("localhost",9999)
db=client.fit5148_assignment
db.climate_historic.drop()
climate_historic=db.climate_historic
climate_historic.insert_many(entire_data)
result=climate_historic.find()
for document in result:
    pprint(document)