from flask import Flask , redirect, render_template, request
import os
import controller
from datetime import date
from dateutil import relativedelta


import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('werkzeug').setLevel(logging.INFO)


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['DEBUG'] = True
log = logging.getLogger(__name__)

@app.route('/')
def index(entrydate=date.today()):    
    if not controller.is_database_configured_correctly():
        return render_template('error.html')
    if controller.does_config_exist():        
        stringdate = entrydate.strftime('%Y-%m-%d')
        log.debug(f'loading main.html with date {entrydate}')
        return render_template('main.html', date_to_record=stringdate)      
    else:
        log.warning('Database in empty, redirecting to setconfig.html')
        return render_template('setconfig.html') 

@app.route ('/savemileage', methods=['POST'])
def save_mileage():
    formdata = request.form
    formdatadate=formdata['date'] 
    formdatamileage=formdata['mileage']
    controller.save_mileage_from_formdata(formdatadate, formdatamileage)
    return render_template('main.html')

@app.route('/saveconfig', methods=['POST'])
def saveconfig():

    formresults = request.form
    log.debug(f'submitted form data{formresults}')
    if controller.check_config_form(formresults):
        controller.save_initial_dataset(formresults)
        return 'configsaved'
    
    else:      
        return 'config not good'      


@app.route('/mileagehistory')
def mileage_history():
    mileage_history = controller.get_mileage_data()
    log.debug(f'rendering template for mileage history: Mileage data: \n{mileage_history}')
    return render_template('mileagehistory.html', mileage_history=mileage_history)





@app.route('/stats')
def return_statistics():
    return "statistics"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)