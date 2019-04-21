from pymongo import MongoClient
from pprint import pprint


client = MongoClient()

db = client.fit5148_db

units = db.units


if __name__ == "__main__":
