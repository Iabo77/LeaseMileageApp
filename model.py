from pymongo import MongoClient
import os
import logging

log = logging.getLogger(__name__)

def get_mileage_document():
    client = MongoClient(os.getenv('CONNECTIONSTRING'))
    database = client[os.getenv('DATABASENAME')]
    collection = database[os.getenv('COLLECTION')]
    mileagedocument = collection.find({})
    if mileagedocument:
        log.debug(f'mileage document collected')
    else:
        log.debug('No mileage document found in database')
    return mileagedocument

def save_mileage_document():
    client = MongoClient(os.getenv('CONNECTIONSTRING'))
    database = client[os.getenv('DATABASENAME')]
    collection = database[os.getenv('COLLECTION')]
    return
