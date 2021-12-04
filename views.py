import requests
from flask import request, abort
from models import update, register, make_admin, calculate_meta, get_sts, get_cfs, get_lws, get_rws, get_cams, get_cms, get_cdms, get_lbs, get_rbs, get_cbs, get_gks, get_squad_by_league
from app import app

@app.route("/")
def default():
    return "<h1>Futstarter backend!</h1><p>To setup the database visit /update, or if you just want to recalculate the meta stats, visit: /calculatemeta</p><p>to GET players from specific leagues: /players/leagues/league/position/ </p><p>to GET squads from specific leagues: /squads/leagues/league/ </p> <p> where league is an integer: (13: PL, 16:Ligue1, 19: Bundes, 31:SerieA, 53: LaLiga) and position is a string (GK, LB, LCB, RCB, RB, LM, LCM, RCM, RM, LST, RST)</p>"

@app.route("/home/")
def home():
    return "<p>Hello, World!</p>"

@app.route('/user/<int:id>/')
def user_profile(id):
    return "Profile page of user #{}".format(id)

@app.route('/api/v1/users', methods=['GET', 'POST'])
def users():
    return None

@app.route('/api/v1/auth/register', methods=['GET', 'POST'])
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

@app.route('/api/v1/auth/admin', methods=['GET, POST'])
def makeadmin():
    if request.method == 'POST':
        request_body = request.get_json()
        res = make_admin(request_body)
        return res
    elif request.method == 'GET':
        return 'Hola GET'
    else:
        abort(405)

@app.route('/update/')
def update_function():
    return update()

@app.route('/calculatemeta/')
def calculatemeta():
    return calculate_meta()

@app.route('/players/leagues/<int:league>/st/')
def getlstslist(league):
    return get_sts(league)

@app.route('/players/leagues/<int:league>/cf/')
def getlcfsslist(league):
    return get_cfs(league)

@app.route('/players/leagues/<int:league>/lw/')
def getlwslist(league):
    return get_lws(league)

@app.route('/players/leagues/<int:league>/rw/')
def getrwslist(league):
    return get_rws(league)

@app.route('/players/leagues/<int:league>/cam/')
def getcamslist(league):
    return get_cams(league)

@app.route('/players/leagues/<int:league>/cm/')
def getcmslist(league):
    return get_cms(league)

@app.route('/players/leagues/<int:league>/cdm/')
def getcdmslist(league):
    return get_cdms(league)

@app.route('/players/leagues/<int:league>/lb/')
def getlbslist(league):
    return get_lbs(league)

@app.route('/players/leagues/<int:league>/cb/')
def getcbslist(league):
    return get_cbs(league)

@app.route('/players/leagues/<int:league>/rb/')
def getrbslist(league):
    return get_rbs(league)

@app.route('/players/leagues/<int:league>/gks/')
def getgkslist(league):
    return get_gks(league)

@app.route('/squads/leagues/<int:league>/')
def getplsquadlist(league):
    return get_squad_by_league(league)



# @app.route("/showmeta/")
# def show():
#     return showmeta()



# @app.route("/api/v1/players/<player_id>", methods=['GET'])
# def get_players(player_id):
#     if request.method == 'GET':
#      return 'Hello' + player_id 




# @app.route("/users/<id>", methods=['GET'])
#     user = User.query.filter_by(id=<id>) 
#     def getUser():
#         return jsonify(user)

# @app.route("/users", methods=['GET'])
#     users = User.query.all() 
#     def getUsers():
#         return jsonify(user) 