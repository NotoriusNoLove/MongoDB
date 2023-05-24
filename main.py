import pymongo
import json
from pprint import pprint
import db


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


def drop_collection(collection):
    collection.drop()
    print(f'[*] {collection} удалена')


def initDB():
    drop_collection(db.goods)
    drop_collection(db.providers)
    drop_collection(db.purchasers)
    drop_collection(db.purchases)
    drop_collection(db.supplies)
