"""
Нет комментариев
"""

from celery import Celery

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.settings import Settings

app = Flask(__name__)
app.config.from_object(Settings)


db = SQLAlchemy(app)


def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    # print(celery.conf)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(app)

from models import *
from view import *