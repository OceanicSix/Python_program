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