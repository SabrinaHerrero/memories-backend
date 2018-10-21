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
manager.create_api(Date, methods=['GET','POST'], url_prefix=None)
manager.create_api(Image, methods=['GET','POST'], url_prefix=None)

if __name__ == '__main__':
   api.run(debug=True, host='0.0.0.0', port=80)