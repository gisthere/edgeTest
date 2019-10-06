import datetime
import time

from app import app, db

from flask import request

from models import Measure


@app.route('/input', methods=['POST'])
def hello_world():
    new_measure = Measure(datetime=datetime.datetime.strptime(request.form['datetime'], '%Y-%m-%d %H:%M:%S.%f'),
                          payload=request.form['payload'])
    db.session.add(new_measure)
    db.session.commit()
    print('request', new_measure)
    time.sleep(1)
    return 'Hello World!'
