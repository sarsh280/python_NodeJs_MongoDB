import pymongo
from pymongo import MongoClient
import json
import pandas as pd
from getpass import getpass

class MongoDB(object):
    
    def __init__(self, dBName=None, collectionName=None):

        self.dBName = dBName
        self.collectionName = collectionName

        self.client = MongoClient("localhost", 27017, maxPoolSize=50)

        self.DB = self.client[self.dBName]
        self.collection = self.DB[self.collectionName]

    def put(self, path = None):
        with open(path) as file:
            file_data = json.load(file)
        self.collection.insert_many(file_data, ordered=False)
        print("Data Inserted to Database")

if __name__ == "__main__":
    mongodb = MongoDB(dBName="STM", collectionName="example")

    #Put Command
    # mongodb.put(path= "data.json")

    #Get command
    # for x in mongodb.collection.find():
    #     print(x)

    #Update command
    # mongodb.collection.update_one({"id":"1"}, {"$set":{"Time":"Monday"}})    

    #Delete Command
    # mongodb.collection.delete_one({"id":"1"}) 

    #Drop a collection
    mongodb.collection.drop()

