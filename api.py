from app import Date
from app import Image
from app import app
from app import db
from flask_cors import CORS, cross_origin
from flask import Flask, request
from flask_restless import APIManager

api = Flask(__name__)

CORS(app) 
manager = APIManager(app, flask_sqlalchemy_db=db)

# Created the basic API calls for each model 
manager.create_api(Date, methods=['GET'], url_prefix=None)
manager.create_api(Image, methods=['GET'], url_prefix=None)