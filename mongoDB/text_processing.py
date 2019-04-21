from pymongo import MongoClient
from pprint import pprint


def create_synopsis(myCol):
    unit_code = ""

    for line in synopsis_set:
        if line in unit_code_list:
            unit_code = line
            continue
        elif unit_code == "":
            continue
        else:
            synopsis_record = {
                'unit_code': unit_code,
                'synopsis': line
            }
            myCol.insert(synopsis_record)


def update_synopsis(myCol):
    for keyword in keyword_set:
        for line in myCol.find({'synopsis': {'$regex':keyword}}):
            new_synopsis = line['synopsis'].replace(keyword, keyword.upper())
            myCol.update_many( {'_id':line["_id"]}, {'$set': {"synopsis":new_synopsis}})


def delete_synopsis(myCol):
    for keyword in keyword_set:
        myCol.delete_many({"synopsis":{"$regex":keyword}})

# def delete_synopsis(myCol):
#     pattern = "SOFTWARE|DATA"
#     myCol.remove({'synopsis': {'$regex': pattern}})

##-----------------------------function------------------------


client = MongoClient()

db = client.fit

units = db.units


if __name__ == "__main__":
    file=open("unit_synopsis.txt","r")
    synopsis_set = file.readlines()
    synopsis_set = [line.strip() for line in synopsis_set]
    print(synopsis_set)

    unit_code_list = ['FIT5148', 'FIT9131', 'FIT9132']
    db.synopsis.drop()


#-----------------------insert data-----------------------------
    myCol = db.synopsis
    create_synopsis(myCol)

    # result=myCol.find()
    # for document in result:
    #     pprint(document)

#-----------------------update data-----------------------------
    keyword_set = ['software', 'database', 'programming', 'development', 'reasoning']
    myCol = db.synopsis
    update_synopsis(myCol)

    # result = myCol.find()
    # for document in result:
    #     pprint(document)


#-----------------------delete data-----------------------------
    keyword_set=["SOFTWARE","DATA"]
    myCol=db.synopsis
    delete_synopsis(myCol)

    result = myCol.find()
    for document in result:
        pprint(document)