from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os


# import requests
# from flask import request, abort, send_from_directory
# from models import update, register, login, delete_user, make_admin, calculate_meta, get_sts, get_cfs, get_lws, get_rws, get_cams, get_cms, get_cdms, get_lbs, get_rbs, get_cbs, get_gks, get_squad_by_league
# from app import app
# import base64


app = Flask(__name__, static_folder=os.path.abspath("/static")', static_url_path='')
app.debug = True
# username = "Javier"
password = "ibanez570"
dbname = "futstarter"

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://javier:ibanez570@localhost:5432/futstarter"
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