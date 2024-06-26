from datetime import date
import os
import logging
import model

log = logging.getLogger(__name__)

class MileageData:
    def __init__(self, StartDate, EndDate, AnnualLimit, CostPerMile, RecordedMileage):
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.AnnualLimit = AnnualLimit
        self.CostPerMile = CostPerMile
        self.RecordedMileage = RecordedMileage
    
    
    @classmethod
    def from_database(cls, dbdata):
        return cls(dbdata['StartDate'],dbdata['EndDate'],dbdata['AnnualLimit'],dbdata['CostPerMile'],dbdata['RecordedMileage'])
    
    @property
    def return_default_record():
        StartDate = 2
        EndDate = StartDate #+ 3 years
        AnnualLimit = 10000
        CostPerMile = 0.65
        RecordedMileage = {}
        return MileageData(StartDate, EndDate, AnnualLimit, CostPerMile, RecordedMileage)

    @property
    def format_MileageData_for_db(self):
        return self.__dict__


    

def get_mileage_data_from_database() -> MileageData:
    try:
        databasedata = model.get_mileage_document()    
        if databasedata  :
            log.debug(databasedata)
        mileage_data = MileageData.from_database(databasedata)    
    except:
        log.debug('ERROR: No record found in dbase creating first record')
        mileage_data = MileageData.return_default_record
    return mileage_data 


def insert_new_mileage_record(mileage, date):
    #insert a value for mileage only one entry can exist per date(day) so check and overwrite
    #or create new
    mileage_data = get_mileage_data_from_database()
    ## if date(key) exists - replace
    ## if date does not exist - insert
    ## sort data by date.  - dict function?
    return











        


