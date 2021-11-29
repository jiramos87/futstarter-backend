from models import request_players_by_league, getstrikers, get_meta_ratings, showmeta, getwingers, getcams, getcms, getcdms, getfbs, getcbs, getsquad
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
def getplstrikerslist():
    return getstrikers(13)

@app.route('/players/leagues/pl/wingers/')
def getplwingerslist():
    return getwingers(13)

@app.route('/players/leagues/pl/cams/')
def getplcamslist():
    return getcams(13)

@app.route('/players/leagues/pl/cms/')
def getplcmslist():
    return getcms(13)

@app.route('/players/leagues/pl/cdms/')
def getplcdmslist():
    return getcdms(13)

@app.route('/players/leagues/pl/fbs/')
def getplfbslist():
    return getfbs(13)

@app.route('/players/leagues/pl/cbs/')
def getplcbslist():
    return getcbs(13)

@app.route('/squads/leagues/pl/')
def getplsquadlist():
    return getsquad(13)

@app.route('/players/leagues/ligue1/strikers/')
def getl1strikerslist():
    return getstrikers(16)

@app.route('/players/leagues/ligue1/wingers/')
def getl1wingerslist():
    return getwingers(16)

@app.route('/players/leagues/ligue1/cams/')
def getl1camslist():
    return getcams(16)

@app.route('/players/leagues/ligue1/cms/')
def getl1cmslist():
    return getcms(16)

@app.route('/players/leagues/ligue1/cdms/')
def getl1cdmslist():
    return getcdms(16)

@app.route('/players/leagues/ligue1/fbs/')
def getl1fbslist():
    return getfbs(16)

@app.route('/players/leagues/ligue1/cbs/')
def getl1cbslist():
    return getcbs(16)

@app.route('/squads/leagues/ligue1/')
def getl1squadlist():
    return getsquad(16)

@app.route('/players/leagues/bundes/strikers/')
def getbundesstrikerslist():
    return getstrikers(19)

@app.route('/players/leagues/bundes/wingers/')
def getbundeswingerslist():
    return getwingers(19)

@app.route('/players/leagues/bundes/cams/')
def getbundescamslist():
    return getcams(19)

@app.route('/players/leagues/bundes/cms/')
def getbundescmslist():
    return getcms(19)

@app.route('/players/leagues/bundes/cdms/')
def getbundescdmslist():
    return getcdms(19)

@app.route('/players/leagues/bundes/fbs/')
def getbundesfbslist():
    return getfbs(19)

@app.route('/players/leagues/bundes/cbs/')
def getbundescbslist():
    return getcbs(19)

@app.route('/squads/leagues/bundes/')
def getbundessquadlist():
    return getsquad(19)

@app.route('/players/leagues/seriea/strikers/')
def getserieastrikerslist():
    return getstrikers(31)

@app.route('/players/leagues/seriea/wingers/')
def getserieawingerslist():
    return getwingers(31)

@app.route('/players/leagues/seriea/cams/')
def getserieacamslist():
    return getcams(31)

@app.route('/players/leagues/seriea/cms/')
def getserieacmslist():
    return getcms(31)

@app.route('/players/leagues/seriea/cdms/')
def getserieacdmslist():
    return getcdms(31)

@app.route('/players/leagues/seriea/fbs/')
def getserieafbslist():
    return getfbs(31)

@app.route('/players/leagues/seriea/cbs/')
def getserieacbslist():
    return getcbs(31)

@app.route('/squads/leagues/seriea/')
def getserieasquadlist():
    return getsquad(31)

@app.route('/players/leagues/laliga/strikers/')
def getlaligastrikerslist():
    return getstrikers(53)

@app.route('/players/leagues/laliga/wingers/')
def getlaligawingerslist():
    return getwingers(53)

@app.route('/players/leagues/laliga/cams/')
def getlaligacamslist():
    return getcams(53)

@app.route('/players/leagues/laliga/cms/')
def getlaligacmslist():
    return getcms(53)

@app.route('/players/leagues/laliga/cdms/')
def getcdmslist():
    return getcdms(53)

@app.route('/players/leagues/laliga/fbs/')
def getlaligafbslist():
    return getfbs(53)

@app.route('/players/leagues/laliga/cbs/')
def getlaligacbslist():
    return getcbs(53)

@app.route('/squads/leagues/laliga/')
def getlaligasquadlist():
    return getsquad(53)

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