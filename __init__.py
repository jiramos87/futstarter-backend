from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os

ENV = os.environ
# import requests
# from flask import request, abort, send_from_directory
# from models import update, register, login, delete_user, make_admin, calculate_meta, get_sts, get_cfs, get_lws, get_rws, get_cams, get_cms, get_cdms, get_lbs, get_rbs, get_cbs, get_gks, get_squad_by_league
# from app import app
# import base64


# app = Flask(__name__, static_folder='static', static_url_path='')
app = Flask(__name__, static_folder=os.path.abspath("/static"), static_url_path='')
app.debug = True

if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://javier:ibanez570@localhost:5432/futstarter"
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://namyczudfpxnaf:2d840075e00fc6846392af812a87736d9a9ef90d110c0d45567b358494a2a535@ec2-3-92-119-83.compute-1.amazonaws.com:5432/d3d1mnvm26jdpl"
 
    
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://namyczudfpxnaf:2d840075e00fc6846392af812a87736d9a9ef90d110c0d45567b358494a2a535@ec2-3-92-119-83.compute-1.amazonaws.com:5432/d3d1mnvm26jdpl"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///futstarter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
app.config["JWT_SECRET_KEY"] = "serverkey"  
jwt = JWTManager(app)

CORS(app)

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

def getApp():
    return app

if __name__ == "__main__":  
    from views import *
    app.run()