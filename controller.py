from datetime import datetime
import os
import logging

log = logging.getLogger(__name__)

class MileageData:
    def __init__(self, StartDate, EndDate, AnnualLimit, CostPerMile, RecordedMileage):
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.AnnualLimit = 10000
        self.CostPerMile = 0.065
        self.RecordedMileage = []

def insert_new_mileage_entry():
    #insert a value for mileage only one entry can exist per date(day) so check and overwrote
    #or create new
    return






        


