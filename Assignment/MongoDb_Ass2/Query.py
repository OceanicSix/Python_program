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
# result=hotspot_historic.find({"$and":[{"surface_temperature_celcius":{"$gt":65}},
#                                       {"surface_temperature_celcius":{"$lt":100}}]},
#                              {"_id":0,"latitude":1,"longitude":1,"surface_temperature_celcius":1,"confidence":1})
#
# myprint(result)

#Q2.c

result=climate_historic.aggregate([{"$match":{"$or":[{"date":"15/12/2017"},{"date":"16/12/2017"}]}},
                                   {"$lookup":
                                        {
                                            "from":"hotspot_historic",
                                            "localField":"date",
                                            "foreignField":"date",
                                            "as":"surface_temperatures"
                                        }
                                    },
                                   {"$project":{"_id":0,"date":1,"air_temperature_celcius":1,"relative_humidity":1,
                                                "max_wind_speed":1,"surface_temperatures.surface_temperature_celcius":1,"surface_temperatures.datetime":1}}

])
myprint(result)

#Q2.d
# result=hotspot_historic.aggregate([{"$match":{"$and":[{"confidence":{"$gt":80}},{"confidence":{"$lt":100}}]}},
#                                    {
#                                        "$lookup":
#                                            {
#                                             "from":"climate_historic",
#                                             "localField":"date",
#                                             "foreignField":"date",
#                                             "as":"air_temperatures"
#                                             }
#                                    },
#                                    {"$project":{"_id":0,"datetime":1,"air_temperatures.air_temperature_celcius":1,"surface_temperature_celcius":1,
#                                                 "confidence":1}}
#                                    ])
# myprint(result)


#Q2.e
# result=hotspot_historic.find({},{"_id":0}).sort("surface_temperature_celcius",pymongo.DESCENDING).limit(10)
# myprint(result)

#Q2.f
# result=hotspot_historic.aggregate([{"$group":{"_id":"$date","number_of_fire":{"$sum":1}}}])
# myprint(result)


#Q2.g
# result=hotspot_historic.aggregate([{"$group":{"_id":"$date","average_surface_temperature":{"$avg":"$surface_temperature_celcius"}}}])
# myprint(result)
