from models import request_players_by_league, getstrikers, get_meta_ratings, showmeta, getwingers, getcams, getcms, getcdms, getfbs, getcbs, getplsquad
from app import app

@app.route("/home/")
def home():
    return "<p>Hello, World!</p>"

@app.route('/user/<int:id>/')
def user_profile(id):
    return "Profile page of user #{}".format(id)

@app.route('/calculatemeta/')
def getmeta():
    return get_meta_ratings()

@app.route('/players/leagues/pl/strikers/')
def getstrikerslist():
    return getstrikers(13)

@app.route('/players/leagues/pl/wingers/')
def getwingerslist():
    return getwingers(13)

@app.route('/players/leagues/pl/cams/')
def getcamslist():
    return getcams(13)

@app.route('/players/leagues/pl/cms/')
def getcmslist():
    return getcms(13)

@app.route('/players/leagues/pl/cdms/')
def getcdmslist():
    return getcdms(13)

@app.route('/players/leagues/pl/fbs/')
def getfbslist():
    return getfbs(13)

@app.route('/players/leagues/pl/cbs/')
def getcbslist():
    return getcbs(13)

@app.route('/squads/leagues/pl/')
def getplsquadlist():
    return getplsquad()

@app.route("/updateplayerdb/", methods=['GET','POST'])
def updateplayers():
    return request_players_by_league()

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