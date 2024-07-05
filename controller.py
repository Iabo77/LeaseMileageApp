from datetime import date
import os
import logging
import model
import datetime
from dateutil.relativedelta import relativedelta

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def save_config(StartDate, TermLength, AnnualMileageLimit, PricePerMile):


    return

def save_mileage_entry(date, mileage):
    return

def get_mileage_data():
    return

def does_config_exist():       
    if model.get_config():
        log.debug('config exists')
        is_blank = True
    else:
        is_blank = False
    return is_blank

def does_mileage_data_exists():
    count = len(model.get_mileage_list())
    log.debug(f'Mileage data exists check: results returned = {count}')
    if count >= 1:
        return True
    else:
        return False
    

def is_database_configured_correctly():
    mileagedata = does_mileage_data_exists()
    configdata = does_config_exist()

    if mileagedata and configdata:
        return True
    elif not mileagedata and not configdata:
        return True
    else:
        log.error('Database is not configured correctly; either maileage or config data exists without the other')
        return False
    