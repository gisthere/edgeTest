from app import db


class ManipulatorStatus(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime())
    status = db.Column(db.String)

    def __init__(self, datetime, status):
        self.datetime = datetime
        self.status = status

    def __repr__(self):
        return f'{self.id} {self.datetime} {self.status}'

