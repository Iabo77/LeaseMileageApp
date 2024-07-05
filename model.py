from pymongo import MongoClient
import os
import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('pymongo').setLevel(logging.WARNING)
logging.getLogger('werkzeug').setLevel(logging.WARNING)

client = MongoClient(os.getenv('CONNECTION_STRING'))
database = client[os.getenv('DATABASENAME')]
collection = database[os.getenv('COLLECTION')]


def get_mileage_list():
    return list(collection.find({"type": "mileage"}))


def get_config():
    config = collection.find_one({"type": "config"})    
    log.debug(f'config pulled from databse: {config}')
    return config

def save_mileage(date, new_mileage): 
    collection.update_one(
        {"type": "mileage", "date": date},
        {"$set": {"mileage": new_mileage}},
        upsert=True
    )

def save_config(configdict):
    collection.update_one(
        {"type":"config"},
        {"$set":configdict}
    )

