import datetime

from app import celery, db
from models import Measure


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5.0, manipulate.s(), name='add every 5')


@celery.task
def manipulate():
    print('manipulate')


@celery.task()
def proceed_request(form):
    new_measure = Measure(datetime=datetime.datetime.strptime(form['datetime'], '%Y-%m-%d %H:%M:%S.%f'),
                          payload=form['payload'])
    db.session.add(new_measure)
    db.session.commit()
