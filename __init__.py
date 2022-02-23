from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os

from flask import jsonify, request, abort, send_from_directory
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from models import db
#from models import register, login, search_players, get_player_by_id, save_squad, get_user_squads, delete_all_squads, delete_user, make_admin, calculate_meta, get_csts, get_cfs, get_lws, get_rws, get_ccams, get_ccms, get_ccdms, get_lbs, get_rbs, get_ccbs, get_gks, get_squad_by_league, update
from models import *

ENV = os.environ
# import requests
# from flask import request, abort, send_from_directory
# from models import update, register, login, delete_user, make_admin, calculate_meta, get_sts, get_cfs, get_lws, get_rws, get_cams, get_cms, get_cdms, get_lbs, get_rbs, get_cbs, get_gks, get_squad_by_league
# from app import app
# import base64


# app = Flask(__name__, static_folder='static', static_url_path='')
flask_app = Flask(__name__, static_folder=os.path.abspath("/static"), static_url_path='')
flask_app.debug = True
FLASK_ENV = 'production'

is_prod = os.environ.get('IS_HEROKU', None)

if is_prod:
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://javier:ibanez570@localhost:5432/futstarter"
else:
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://namyczudfpxnaf:2d840075e00fc6846392af812a87736d9a9ef90d110c0d45567b358494a2a535@ec2-3-92-119-83.compute-1.amazonaws.com:5432/d3d1mnvm26jdpl"
 
    
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://namyczudfpxnaf:2d840075e00fc6846392af812a87736d9a9ef90d110c0d45567b358494a2a535@ec2-3-92-119-83.compute-1.amazonaws.com:5432/d3d1mnvm26jdpl"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///futstarter.db'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
flask_app.config['JSON_SORT_KEYS'] = False
flask_app.config["JWT_SECRET_KEY"] = "serverkey"  
jwt = JWTManager(flask_app)

CORS(flask_app)

#db = SQLAlchemy(app)
db.init_app(flask_app)
migrate = Migrate(flask_app, db)

def getApp():
    return app

@flask_app.route("/")
def serve():
    #return send_from_directory(app.static_folder, 'client/build/index.html')
    return "<h1>Futstarter backend!</h1><p>To setup the database visit /api/v1/setup/update/, or if you just want to recalculate the meta stats, visit: /api/v1/setup/calculatemeta/</p><p>to GET players from specific leagues: /api/v1/players/leagues/league/position/ </p><p>to GET squads from specific leagues: /api/v1/squads/leagues/league/ </p> <p> where league is an integer: (13: PL, 16:Ligue1, 19: Bundes, 31:SerieA, 53: LaLiga) and position is a string (GK, LB, LCB, RCB, RB, LM, LCM, RCM, RM, LST, RST)</p>"

@flask_app.route("/home/")
def home():
    return "<p>Hello, World!</p>"

@flask_app.route('/user/<int:id>/')
def user_profile(id):
    return "Profile page of user #{}".format(id)

@flask_app.route('/api/v1/users', methods=['GET', 'POST'])
def users():
    return None

@flask_app.route('/api/v1/auth/register', methods=['GET', 'POST'])
def register_fn():
    if request.method == 'POST':
        request_body = request.get_json()
        res = register(request_body)
        return res
        #return 'hola post'
    elif request.method == 'GET':
        return 'Hola GET'
    else:
        abort(405)


@flask_app.route("/api/v1/auth/login", methods=["POST"])
def create_token():
    if request.method == 'POST':
        req_body = request.get_json()
        return login(req_body)
    elif request.method == 'GET':
        return 'This method only accepts POST'
    else:
        abort(405)
    
@flask_app.route("/api/v1/players/search", methods=["POST"])
def playersearch():
    if request.method == 'POST':
        req_body = request.get_json()
        return search_players(req_body)
    elif request.method == 'GET':
        return 'This method only accepts POST'
    else:
        abort(405)

@flask_app.route("/api/v1/players/<int:id>", methods=["GET"])
def getplayerbyid(id):
    return get_player_by_id(id)
    

@flask_app.route("/user/savesquad", methods=["POST"])
@jwt_required()
def savesquad():
    if request.method == 'POST':
        current_user = get_jwt_identity()
        req_body = request.get_json()
        # Access the identity of the current user with get_jwt_identity
        
        return save_squad(req_body, current_user)
    elif request.method == 'GET':
        return 'This method only accepts POST'
    else:
        abort(405)

@flask_app.route("/user/getusersquads", methods=["POST"])
@jwt_required()
def getusersquads():
    if request.method == 'POST':
        current_user = get_jwt_identity()
        print(current_user)
        # Access the identity of the current user with get_jwt_identity
        
        return get_user_squads(current_user)
    elif request.method == 'GET':
        return 'This method only accepts POST'
    else:
        abort(405)

@flask_app.route("/user/deletesquads/<int:id>")
def delete_squads(id):
    return delete_all_squads(id)

@flask_app.route('/api/v1/auth/delete/<int:id>')
def delete(id):
    return delete_user(id)

@flask_app.route('/api/v1/auth/admin', methods=['GET, POST'])
def makeadmin():
    if request.method == 'POST':
        request_body = request.get_json()
        res = make_admin(request_body)
        return res
    elif request.method == 'GET':
        return 'Hola GET'
    else:
        abort(405)

@flask_app.route('/api/v1/setup/update/')
def update_function():
    return update()

@flask_app.route('/api/v1/setup/calculatemeta/')
def calculatemeta():
    return calculate_meta()

@flask_app.route('/api/v1/static/<path:path>')
def send_image(path):
    return send_from_directory(flask_app.static_folder, path)


@flask_app.route('/api/v1/players/leagues/<int:league>/cst/')
def getcstslist(league):
    return get_csts(league)

@flask_app.route('/api/v1/players/leagues/<int:league>/cf/')
def getcfslist(league):
    return get_cfs(league)

@flask_app.route('/api/v1/players/leagues/<int:league>/lw/')
def getlwslist(league):
    return get_lws(league)

@flask_app.route('/api/v1/players/leagues/<int:league>/rw/')
def getrwslist(league):
    return get_rws(league)

@flask_app.route('/api/v1/players/leagues/<int:league>/ccam/')
def getccamslist(league):
    return get_ccams(league)

@flask_app.route('/api/v1/players/leagues/<int:league>/ccm/')
def getccmslist(league):
    return get_ccms(league)

@flask_app.route('/api/v1/players/leagues/<int:league>/ccdm/')
def getccdmslist(league):
    return get_ccdms(league)

@flask_app.route('/api/v1/players/leagues/<int:league>/lb/')
def getlbslist(league):
    return get_lbs(league)

@flask_app.route('/api/v1/players/leagues/<int:league>/ccb/')
def getccbslist(league):
    return get_ccbs(league)

@flask_app.route('/api/v1/players/leagues/<int:league>/rb/')
def getrbslist(league):
    return get_rbs(league)

@flask_app.route('/api/v1/players/leagues/<int:league>/gks/')
def getgkslist(league):
    return get_gks(league)

@flask_app.route('/api/v1/squads/leagues/<int:league>/')
def getplsquadlist(league):
    return get_squad_by_league(league)

if __name__ == "__main__":  
    #from views import *
    flask_app.run()