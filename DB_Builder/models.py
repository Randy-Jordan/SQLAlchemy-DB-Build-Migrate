from DB_Builder import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

class Users(db.Model):
    __table_name__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    pw = db.Column(db.String(255),nullable=False)
    uid = db.Column(db.String(255), unique=True, nullable=False)
    sid = db.Column(db.String(255), unique=True)
    llogin = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    jdate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    

    def __init__(self,uname,email,pw,uid,sid,llogin,jdate):
        self.uname = uname
        self.email = email
        self.pw = pw
        self.uid = uid
        self.sid = sid
        self.llogin = llogin
        self.jdate = jdate


