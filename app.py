from flask import Flask , redirect, render_template, request
import os
import controller
from datetime import date


import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('werkzeug').setLevel(logging.INFO)


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['DEBUG'] = True

log = logging.getLogger(__name__)

@app.route('/')
def index():    
    if not controller.is_database_configured_correctly():
        return render_template('error.html')
    if controller.does_config_exist():        
        return render_template('main.html')      
    else:
        log.warning('Database in empty, redirecting to setconfig.html')
        return render_template('setconfig.html') 

@app.route ('/savemileage')
def save_mileage():
      

    return 

@app.route('/mileagehistory')
def mileage_history():
    #mileagedata = controller.get_mileage_data_from_database()
    mileage_records = {'somedate':10101, 'someotherdate': 119191 }     
    return render_template('mileagehistory.html', mileage_records=mileage_records)



@app.route('/stats')
def return_statistics():
    return "statistics"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)