from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    level = db.Column(db.Integer())

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return '<id {}>'.format(self.name)