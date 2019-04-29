import pymongo
from pymongo import MongoClient
from pprint import pprint

def myprint(result):
    for documnent in result:
        pprint(documnent)



client=MongoClient("localhost",9999)
db=client.fit5148_assignment
climate_historic=db.climate_historic
hotspot_historic=db.hotspot_historic

#Q2.a
# result=climate_historic.find({"date":"10/12/2017"},{"_id":0})
# myprint(result)

#Q2.b
result=hotspot_historic.find({"$and":[{"surface_temperature_celcius":{"$gt":65}},
                                      {"surface_temperature_celcius":{"$lt":100}}]})

myprint(result)