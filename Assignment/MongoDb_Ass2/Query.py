import pymongo
from pymongo import MongoClient
from pprint import pprint


client=MongoClient("localhost",9999)
db=client.fit5148_assignment
climate_historic=db.climate_historic
#Q2.a

