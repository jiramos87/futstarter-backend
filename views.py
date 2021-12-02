from models import update, get_strikers, get_wingers, get_cams, get_cms, get_cdms, get_fbs, get_cbs, get_squad_by_league
from app import app

@app.route("/home/")
def home():
    return "<p>Hello, World!</p>"

@app.route('/user/<int:id>/')
def user_profile(id):
    return "Profile page of user #{}".format(id)

@app.route('/update/')
def update_function():
    return update()

@app.route('/players/leagues/pl/strikers/')
def getplstrikerslist():
    return get_strikers(13)

@app.route('/players/leagues/pl/wingers/')
def getplwingerslist():
    return get_wingers(13)

@app.route('/players/leagues/pl/cams/')
def getplcamslist():
    return get_cams(13)

@app.route('/players/leagues/pl/cms/')
def getplcmslist():
    return get_cms(13)

@app.route('/players/leagues/pl/cdms/')
def getplcdmslist():
    return get_cdms(13)

@app.route('/players/leagues/pl/fbs/')
def getplfbslist():
    return get_fbs(13)

@app.route('/players/leagues/pl/cbs/')
def getplcbslist():
    return get_cbs(13)

@app.route('/squads/leagues/<int:league>/')
def getplsquadlist(league):
    return get_squad_by_league(league)

@app.route('/players/leagues/ligue1/strikers/')
def getl1strikerslist():
    return get_strikers(16)

@app.route('/players/leagues/ligue1/wingers/')
def getl1wingerslist():
    return get_wingers(16)

@app.route('/players/leagues/ligue1/cams/')
def getl1camslist():
    return get_cams(16)

@app.route('/players/leagues/ligue1/cms/')
def getl1cmslist():
    return get_cms(16)

@app.route('/players/leagues/ligue1/cdms/')
def getl1cdmslist():
    return get_cdms(16)

@app.route('/players/leagues/ligue1/fbs/')
def getl1fbslist():
    return get_fbs(16)

@app.route('/players/leagues/ligue1/cbs/')
def getl1cbslist():
    return get_cbs(16)

@app.route('/squads/leagues/ligue1/')
def getl1squadlist():
    return get_squad_by_league(16)

@app.route('/players/leagues/bundes/strikers/')
def getbundesstrikerslist():
    return get_strikers(19)

@app.route('/players/leagues/bundes/wingers/')
def getbundeswingerslist():
    return get_wingers(19)

@app.route('/players/leagues/bundes/cams/')
def getbundescamslist():
    return get_cams(19)

@app.route('/players/leagues/bundes/cms/')
def getbundescmslist():
    return get_cms(19)

@app.route('/players/leagues/bundes/cdms/')
def getbundescdmslist():
    return get_cdms(19)

@app.route('/players/leagues/bundes/fbs/')
def getbundesfbslist():
    return get_fbs(19)

@app.route('/players/leagues/bundes/cbs/')
def getbundescbslist():
    return get_cbs(19)

@app.route('/squads/leagues/bundes/')
def getbundessquadlist():
    return get_squad_by_league(19)

@app.route('/players/leagues/seriea/strikers/')
def getserieastrikerslist():
    return get_strikers(31)

@app.route('/players/leagues/seriea/wingers/')
def getserieawingerslist():
    return get_wingers(31)

@app.route('/players/leagues/seriea/cams/')
def getserieacamslist():
    return get_cams(31)

@app.route('/players/leagues/seriea/cms/')
def getserieacmslist():
    return get_cms(31)

@app.route('/players/leagues/seriea/cdms/')
def getserieacdmslist():
    return get_cdms(31)

@app.route('/players/leagues/seriea/fbs/')
def getserieafbslist():
    return get_fbs(31)

@app.route('/players/leagues/seriea/cbs/')
def getserieacbslist():
    return get_cbs(31)

@app.route('/squads/leagues/seriea/')
def getserieasquadlist():
    return get_squad_by_league(31)

@app.route('/players/leagues/laliga/strikers/')
def getlaligastrikerslist():
    return get_strikers(53)

@app.route('/players/leagues/laliga/wingers/')
def getlaligawingerslist():
    return get_wingers(53)

@app.route('/players/leagues/laliga/cams/')
def getlaligacamslist():
    return get_cams(53)

@app.route('/players/leagues/laliga/cms/')
def getlaligacmslist():
    return get_cms(53)

@app.route('/players/leagues/laliga/cdms/')
def getcdmslist():
    return get_cdms(53)

@app.route('/players/leagues/laliga/fbs/')
def getlaligafbslist():
    return get_fbs(53)

@app.route('/players/leagues/laliga/cbs/')
def getlaligacbslist():
    return get_cbs(53)

@app.route('/squads/leagues/laliga/')
def getlaligasquadlist():
    return get_squad_by_league(53)



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