from models import request_players_by_league, getplplayer, getplList
from app import app

@app.route("/home/")
def home():
    return "<p>Hello, World!</p>"

@app.route('/user/<int:id>/')
def user_profile(id):
    return "Profile page of user #{}".format(id)

@app.route('/plplayer/<int:resource_id>')
def plplayer(resource_id):
    return getplplayer(resource_id)

@app.route('/getpllist/')
def getpllist():
    return getplList()

@app.route("/getplsquads/", methods=['GET','POST'])
def getplsquads():
    return request_players_by_league()



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