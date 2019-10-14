from app import db


class Measure(db.Model):
    __tablename__ = 'measure'

    id = db.Column(db.Integer, primary_key=True, index=True)
    datetime = db.Column(db.DateTime(), index=True)
    payload = db.Column(db.Integer)
    sensor_name = db.Column(db.String(12))

    def __init__(self, datetime, payload, name):
        self.datetime = datetime
        self.payload = payload
        self.sensor_name = name

    def __repr__(self):
        return f'{self.id} {self.datetime} {self.payload} {self.sensor_name}'

