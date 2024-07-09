from pymongo import MongoClient
import os
import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('pymongo').setLevel(logging.WARNING)
logging.getLogger('werkzeug').setLevel(logging.WARNING)

def connect_to_db():
    cstring = os.getenv('CONNECTION_STRING')
    collection=None
    log.debug(f'connecing to database: CSTRING: {cstring}')
    try:
        client = MongoClient(os.getenv('CONNECTION_STRING'))
        database = client[os.getenv('DATABASENAME')]
        collection = database[os.getenv('COLLECTION')]
    except Exception as e:
        log.debug(f'error connecting to databse\n error:\n {e}')
    return collection

collection = connect_to_db()

def get_mileage_list():
    mileagelist = list(collection.find({"type": "mileage"}))
    log.debug(f'mileage list returned from DB:\n {mileagelist}')
    return mileagelist


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
        {"$set":configdict},
        upsert=True
    )

def delete_mileage_by_date(date):


    return

def delete_all_mileage():
    return


