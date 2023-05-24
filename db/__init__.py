from os import environ

from dotenv import find_dotenv, load_dotenv

from pymongo import MongoClient


load_dotenv(find_dotenv())

cluster = MongoClient(environ.get('CONNECTION_PROPERTIES'))

db = cluster.shad112_Gaganovs_petroject


goods = db['goods']
providers = db['providers']
purchasers = db['purchasers']
purchases = db['purchases']
supplies = db['supplies']
