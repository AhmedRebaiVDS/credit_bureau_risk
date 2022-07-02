from app import db
from datetime import datetime

class User(db.Document) :
    name=db.StringField(max_length=50, required=True)
    email=db.StringField(max_length=50, required=True, unique=True)
    password=db.StringField(max_length=100, required=True)
    reset_token=db.StringField(max_length=500,default="")
    expire_token=db.DateField(max_length=50 ,default=datetime.now())