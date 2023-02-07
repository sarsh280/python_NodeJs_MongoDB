# Lab Assignment 3(CSV to Database)
# Name: Arshdeep Singh (8758644)
# Date: 11-08-2022

# Libraries
import pymongo
from pymongo import MongoClient
import pandas as pd
import json

class MongoDB(object):

# Data Base initialization #
    def __init__(self, dBName=None, collectionName=None):

        self.dBName = dBName
        self.collectionName = collectionName

        self.client = MongoClient("localhost", 27017, maxPoolSize=50)

        self.DB = self.client[self.dBName]
        self.collection = self.DB[self.collectionName]

# Fetching Data from CSV file and insert into database #
    def InsertCSVData(self, path=None):
        df = pd.read_csv(path)
        data = df.to_dict('records')

        self.collection.insert_many(data, ordered=False)
        print("Data Inserted to Database")
        # print(data)
    
# Put data
    def put(self,path=None):
        with open(path) as file:
            file_data = json.load(file)
        self.collection.insert_many(file_data, ordered=False)
        print("Data Inserted to Database")

if __name__ == "__main__":
    mongodb = MongoDB(dBName = 'STM', collectionName='stmData')
    # mongodb.InsertCSVData(path="data.csv")
    mongodb.put(path="data.json")




