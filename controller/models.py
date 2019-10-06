from app import db


class Measure(db.Model):
    __tablename__ = 'measure'

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime())
    payload = db.Column(db.Integer)

    def __init__(self, datetime, payload):
        self.datetime = datetime
        self.payload = payload

    def __repr__(self):
        return f'{self.id} {self.datetime} {self.payload}'

