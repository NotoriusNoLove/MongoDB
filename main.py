import pymongo
import json
from pprint import pprint
from db import db


a = db['goods']


def insert_collection(collection, file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        collection.insert_many(data)
        for item in data:
            print(f"[*] inserting {item} in {collection.name}")


def update_collection(collection, filter_key, filter_value, text_key, text_value):
    collection.find_one_and_update({filter_key: filter_value}, {
                                   "$set": {text_key: text_value}})

    pprint(f"[*] Updating {collection.name} with {text_key, text_value}")


def delete_data(collection, filter):
    collection.delete_one(filter)
    print(f"[*] deleting {filter} in {collection.name}")
