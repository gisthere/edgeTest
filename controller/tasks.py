import datetime
import json

import redis
import requests
from sqlalchemy import func

from app import celery, db, Settings
from models import Measure
from utils import Socket
interval = Settings.MANIPULATE_INTERVAl


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(interval, manipulate.s())


@celery.task(time_limit=1)
def manipulate():
    interval_ago = datetime.datetime.utcnow() - datetime.timedelta(seconds=5)
    result = db.session\
        .query(Measure.sensor_name, func.avg(Measure.payload))\
        .filter(Measure.datetime > interval_ago)\
        .group_by(Measure.sensor_name) \
        .all()
    threshold = 2.5
    thrasholded_sensors = 0
    for sensor in result:
        if sensor[1] > threshold:
            thrasholded_sensors += 1
    manipulate_result = 'Up' if thrasholded_sensors > 4 else 'Down'
    manipulator_data = {
        'datetime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),
        'status': manipulate_result,
    }
    res_bytes = bytes(json.dumps(manipulator_data), 'utf-8')
    sock = Socket('manipulator', 5005)
    with sock as conn:
        conn.send(res_bytes)
    requests.post('http://web:5000/manipulator', data=manipulator_data)


@celery.task(time_limit=interval-1, soft_time_limit=1)
def proceed_request(form):
    new_measure = Measure(datetime=datetime.datetime.strptime(form['datetime'], '%Y-%m-%d %H:%M:%S.%f'),
                          payload=form['payload'],
                          name=form['sensor'])
    db.session.add(new_measure)
    db.session.commit()
    interval_ago = datetime.datetime.utcnow() - datetime.timedelta(seconds=5)
    print(db.session \
        .query(Measure) \
        .filter(Measure.datetime > interval_ago).count())