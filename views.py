from flask import jsonify, request, abort, send_from_directory
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from models import delete_all_squads, update, register, login, search_players, get_player_by_id, save_squad, get_user_squads, delete_all_squads, delete_user, make_admin, calculate_meta, get_csts, get_cfs, get_lws, get_rws, get_ccams, get_ccms, get_ccdms, get_lbs, get_rbs, get_ccbs, get_gks, get_squad_by_league
from __init__ import app

@app.route("/")
def serve():
    #return send_from_directory(app.static_folder, 'client/build/index.html')
    return "<h1>Futstarter backend!</h1><p>To setup the database visit /api/v1/setup/update/, or if you just want to recalculate the meta stats, visit: /api/v1/setup/calculatemeta/</p><p>to GET players from specific leagues: /api/v1/players/leagues/league/position/ </p><p>to GET squads from specific leagues: /api/v1/squads/leagues/league/ </p> <p> where league is an integer: (13: PL, 16:Ligue1, 19: Bundes, 31:SerieA, 53: LaLiga) and position is a string (GK, LB, LCB, RCB, RB, LM, LCM, RCM, RM, LST, RST)</p>"

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


@app.route("/api/v1/auth/login", methods=["POST"])
def create_token():
    if request.method == 'POST':
        req_body = request.get_json()
        return login(req_body)
    elif request.method == 'GET':
        return 'This method only accepts POST'
    else:
        abort(405)
    
@app.route("/api/v1/players/search", methods=["POST"])
def playersearch():
    if request.method == 'POST':
        req_body = request.get_json()
        return search_players(req_body)
    elif request.method == 'GET':
        return 'This method only accepts POST'
    else:
        abort(405)

@app.route("/api/v1/players/<int:id>", methods=["GET"])
def getplayerbyid(id):
    return get_player_by_id(id)
    

@app.route("/user/savesquad", methods=["POST"])
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

@app.route("/user/getusersquads", methods=["POST"])
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

@app.route("/user/deletesquads/<int:id>")
def delete_squads(id):
    return delete_all_squads(id)

@app.route('/api/v1/auth/delete/<int:id>')
def delete(id):
    return delete_user(id)

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

@app.route('/api/v1/setup/update/')
def update_function():
    return update()

@app.route('/api/v1/setup/calculatemeta/')
def calculatemeta():
    return calculate_meta()

@app.route('/api/v1/static/<path:path>')
def send_image(path):
    return send_from_directory(app.static_folder, path)


@app.route('/api/v1/players/leagues/<int:league>/cst/')
def getcstslist(league):
    return get_csts(league)

@app.route('/api/v1/players/leagues/<int:league>/cf/')
def getcfslist(league):
    return get_cfs(league)

@app.route('/api/v1/players/leagues/<int:league>/lw/')
def getlwslist(league):
    return get_lws(league)

@app.route('/api/v1/players/leagues/<int:league>/rw/')
def getrwslist(league):
    return get_rws(league)

@app.route('/api/v1/players/leagues/<int:league>/ccam/')
def getccamslist(league):
    return get_ccams(league)

@app.route('/api/v1/players/leagues/<int:league>/ccm/')
def getccmslist(league):
    return get_ccms(league)

@app.route('/api/v1/players/leagues/<int:league>/ccdm/')
def getccdmslist(league):
    return get_ccdms(league)

@app.route('/api/v1/players/leagues/<int:league>/lb/')
def getlbslist(league):
    return get_lbs(league)

@app.route('/api/v1/players/leagues/<int:league>/ccb/')
def getccbslist(league):
    return get_ccbs(league)

@app.route('/api/v1/players/leagues/<int:league>/rb/')
def getrbslist(league):
    return get_rbs(league)

@app.route('/api/v1/players/leagues/<int:league>/gks/')
def getgkslist(league):
    return get_gks(league)

@app.route('/api/v1/squads/leagues/<int:league>/')
def getplsquadlist(league):
    return get_squad_by_league(league)

