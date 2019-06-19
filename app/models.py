from app import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    level = db.Column(db.Integer())
    user_option = relationship('UserOption', cascade="delete")
    comment = relationship('Comment', cascade="delete")

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
    user_option = relationship("UserOption", cascade="delete")

    def __init__(self, option, level):
        self.option = option
        self.level = level

    def __repr__(self):
        return '<id {}>'.format(self.option)

class UserOption(db.Model):
    __tablename__ = 'user_option'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship("User")
    option_id = db.Column(db.Integer, db.ForeignKey('option.id'))
    option = relationship("Option")
    comment = relationship("Comment", cascade="delete")

class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    user_option_id = db.Column(db.Integer, db.ForeignKey('user_option.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment = db.Column(db.String())
    user_option = relationship("UserOption")
    user = relationship("User")