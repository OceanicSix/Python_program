import pymongo
from pymongo import MongoClient
from pprint import pprint

client=MongoClient()
db=client.fit
db.montours.drop()

montours = db.montours # create collection


#-------------------------insert--------------------

newTour = {"package":"MonITTour",
    "name":"Monash IT Tour",
    "length":1,
    "price":100,
    "location":"Caulfield",
    "organiser" : {
        "faculty": "FIT",
        "person" : "John Smith"
    },
    "tags":["Monash", "FIT", "Caulfield"]}
montours.insert_one(newTour)

newTours = [
{
    "package":"MonArtTour",
    "name":"Monash Art Tour",
    "length":2,
    "price":50,
    "location":"Caulfield",
    "organiser" : {
            "faculty": "Faculty of Arts",
            "person" : "Linda Adams"
    },
    "tags":["Monash", "Art", "Caulfield"]
},
{
    "package":"MonITTour",
    "name":"Monash IT Tour at Clayton",
    "length":3,
    "price":50,
    "location":"Clayton",
    "organiser" : {
            "faculty": "FIT",
            "person" : "Josh Gange"
    },
    "tags":["Monash", "FIT", "Clayton"]
}]
montours.insert_many(newTours)


#-------------------------update-------------------------

result = montours.update_one(
    {"package":"MonITTour"},
    {
    "$set": {
        "name":"Monash IT Faculty Tour"}
    }
)


result=montours.update_one(
    {"package":"MonArtTour"},
    {"$set":
         {"organiser.person":"Katherine McDonald"}
    }
)

result=montours.update_many(
    {"package":"MonITTour"},
    {"$set":
         {"name":"Exciting journey to Monash FIT"}
    }
)

# print(result.matched_count)


#------------------------------replace-------------------
result = montours.replace_one(
    {"name":"Exciting journey to Monash FIT"},
    {"name":"Monash FIT tour"})

# print(result.matched_count)

#-----------------------delete-------------------------

result = montours.delete_one({"package":"MonArtTour"})
# print(result.deleted_count)


result=montours.delete_many({"name":"Monash FIT tour"})
# print(result.deleted_count)


#-----------------------rename-------------------------
montours.rename("monashTours")
monashTours = db.monashTours
monashTours.rename("montours")
montours = db.montours


#---------------------------range query and sorting---------------

result=montours.find(
    {"price":
         {"$gte":50}}).sort("length",pymongo.ASCENDING)

# for document in result:
#     pprint(document)


#--------------------------------index----------------

result = montours.create_index([('organiser.person', pymongo.ASCENDING)], unique=True)



#----------------------------aggregate-------------------------
results = montours.aggregate([{"$group":{"_id":"$package","avg":{"$avg":"$price"}, "count":{"$sum":1}}}])
# for document in results:
#     pprint(document)


#--------------------------------join---------------------------
users = db.users
units = db.units

results = users.aggregate([{
"$lookup":
    {
        "from": "units",
        "localField": "completed_units",
        "foreignField" : "unit_code",
        "as": "completed_units"
    }
},{"$project":{"completed_units._id":0}}])
for document in results:
    pprint(document)