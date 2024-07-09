from datetime import date, datetime
import os
import logging
import model
from dateutil.relativedelta import relativedelta
from operator import itemgetter

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def save_config(StartDate, TermLength, AnnualMileageLimit, PricePerMile):


    return

def save_mileage_from_formdata(submitteddate, submittedmileage):
    date = datetime.strptime(submitteddate, '%Y-%m-%d')
    model.save_mileage(date,submittedmileage)
    return

def get_mileage_data():
    all_mileage = model.get_mileage_list()
    for entry in all_mileage:
        date_to_convert = entry['date']
        entry['date']= date_to_convert.strftime('%Y-%m-%d')
    newlist = sorted(all_mileage, key=itemgetter('date'))
    return newlist

def get_mileage_by_date():
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
        log.error('Database is not configured correctly; either mileage or config data exists without the other')
        return False
    
def check_config_form(configformdata):
    # this validation should be expanded upon
    log.debug(f'config supplied to controller:{configformdata}')

    is_formdata_valid = True
    ## should have form validation..
    if configformdata['startdate'] and configformdata['termlength'] and configformdata['pencepermile'] :
        is_formdata_valid = True
    else:
        is_formdata_valid = False

    return is_formdata_valid

def save_initial_dataset(configformdata):
    startdatestr = configformdata['startdate']
    startdate = datetime.strptime(startdatestr, '%Y-%m-%d')
    termlength = int(configformdata['termlength'])
    pencepermile = float(configformdata['pencepermile'])
    enddate = startdate + relativedelta(years=termlength)

    initialconfigdict = {'type':'config', 'startdate':startdate,'enddate':enddate, 'termlength':termlength, 'pencepermile':pencepermile}
    
    try:
        log.debug (f'saving config file with following data:\n {initialconfigdict}')    
        model.save_config(initialconfigdict)
    except Exception as e:
        log.error(f'Failed to save initial config document to database. ERROR: \n{e}')
        
    try:
        log.debug (f'saving mile file with following data:\n startdate:{startdate}\n mileage:0')    
        model.save_mileage(startdate, 0)
    except Exception as e:
        log.error(f'Failed to save initial mileage document to database. ERROR: \n{e}')
    
    return 





    