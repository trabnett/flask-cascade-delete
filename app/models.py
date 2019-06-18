from app import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    level = db.Column(db.Integer())
    user_option = Relationship('UserOption')

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return '<id {}>'.format(self.name)

class Option(db.Model):
    __tablename__ = 'option'

    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.String())
    level = db.Column(db.Integer())

    def __init__(self, option, level):
        self.option = option
        self.level = level

    def __repr__(self):
        return '<id {}>'.format(self.option)

class UserOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship("User", cascade="delete")
    option_id = db.Column(db.Integer, db.ForeignKey('option.id'))
    option = relationship("Option", cascade="delete")