from . import db # from current package, import db object line 5 in __init__ file for this case
from flask_login import UserMixin
from sqlalchemy.sql import func

#database models(schema) for users and notes
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000)) #max length notes can be
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #dates note was created. func.now() will essentially get us current datetime
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Associates notes with users using foreign key. Since its a one to many relationship,
                                                              # the foreign key is on the 'child' since 1 user can have many notes


class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True) #primary key id
    email = db.Column(db.String(150), unique=True) # emails have to be unique. not dupes. 150 chars in length
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # sets relationship with note table. Foreign key is in lower case but relationship you reference name of class, 'Note' in this case