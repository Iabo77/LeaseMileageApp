from flask import Flask , redirect, render_template, request
import os
import controller
from datetime import date


import logging


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['DEBUG'] = True

log = logging.getLogger(__name__)

@app.route('/')
def enter_mileage(supplied_date = date.today()):
    date_to_record=supplied_date.strftime('%Y-%m-%d') 
    return render_template('main.html', date_to_record = date_to_record)

@app.route ('/savemileage')
def save_mileage():
    number = request.form['number']
    selected_date = request.form['date']
    print (f'{number}:{selected_date}')
    entered_mileage = 10
    specified_date = 2
    #controller.insert_new_mileage_record(entered_mileage, specified_date)

    return redirect()

@app.route('/mileagehistory')
def mileage_history():
    #mileagedata = controller.get_mileage_data_from_database()
    mileage_records = {'soemdate':10101, 'someotherdate': 119191 }     
    return render_template('mileagehistory.html', mileage_records=mileage_records)



@app.route('/stats')
def return_statistics():
    return "statistics"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)