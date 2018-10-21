from login import credentials
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests
# API imports
from flask_cors import CORS, cross_origin
from flask import Flask, request
from flask_restless import APIManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = credentials
#allows for the backend server to run on a seperate domain than the front end
# CORS(app) 
db = SQLAlchemy(app)
# manager = APIManager(app, flask_sqlalchemy_db=db)


class Date(db.Model):
   __tableame__ = 'date'
   date_id = db.Column(db.Integer, primary_key = True, nullable = False)
   title = db.Column(db.String(500), nullable = False)  
   description = db.Column(db.String(5000), nullable = True)
   completed = db.Column(db.Boolean, nullable = False)  
   date = db.Column(db.Date, nullable = True)
   images = db.relationship('Image', backref = 'date', lazy = True)

class Image(db.Model):
   __tableame__ = 'image'
   image_id = db.Column(db.Integer, primary_key = True, nullable = False)
   link = db.Column(db.String(5000), nullable = False)
   description = db.Column(db.String(5000), nullable = True)
   date_id = db.Column(db.Integer, db.ForeignKey('date.date_id'), nullable = False)

# Creates the tables in the specified database using the models 
db.create_all()

#------API Endpoints------#

CORS(app) 
manager = APIManager(app, flask_sqlalchemy_db=db)

# Created the basic API calls for each model 
manager.create_api(Date, methods=['GET','POST'], url_prefix=None)
manager.create_api(Image, methods=['GET','POST'], url_prefix=None)

#------run the app------#

app.run(host='0.0.0.0', port=80)

