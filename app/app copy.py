from enum import unique
from flask import Flask, jsonify, request
import json
#from utils.serializer import Serializer
from flask_sqlalchemy import SQLAlchemy
import requests 

app = Flask(__name__)
app.debug = True
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////example.sqlite"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)

@app.route("/home/")
def home():
    return "<p>Hello, World!</p>"

@app.route('/user/<int:id>/')
def user_profile(id):
    return "Profile page of user #{}".format(id)

@app.route("/getplsquads/", methods=['GET','POST'])
def getplsquads():  
        request_data = { 
            "rarity": 1,
            "league": 13 
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'X-AUTH-TOKEN': '{}'.format(apiKey)
        }
        try:
            
            #plPlayer.query.delete()
        
            response = requests.post('https://futdb.app/api/players/search', json=request_data, headers=headers).json()
            
            for page in range(1, response["page_total"], 1):
                response2 = requests.post(baseUrl+'?page='+str(page), json=request_data, headers=headers).json()
                #print(response["items"])
                for player in response2["items"]:
                    print(player["id"], player["name"])
                    # plPlayer = Player()
                    # plPlayer.id = player["id"]
                    # plPlayer.resource_id = player["resource_id"]
                    # plPlayer.name = player["name"]
                    # plPlayer.common_name = player["common_name"]
                    # plPlayer.name = player["name"]
                    # plPlayer.first_name = player["first_name"]
                    # plPlayer.last_name = player["last_name"]
                    # plPlayer.rarity = player["rarity"]
                    # plPlayer.rarity = player["rarity"]
                    # plPlayer.rating = player["rating"]
                    # plPlayer.nation = player["nation"]
                    # plPlayer.league = player["league"]
                    # plPlayer.position = player["position"]
                    # plPlayer.club = player["club"]
                    # plPlayer.foot = player["foot"]
                    # plPlayer.height = player["height"]
                    # plPlayer.weigth = player["weigth"]
                    # plPlayer.attack_work_rate = player["attack_work_rate"]
                    # plPlayer.defense_work_rate = player["defense_work_rate"]
                    # plPlayer.weak_foot = player["weak_foot"]
                    # plPlayer.skill_moves = player["skill_moves"]
                    # plPlayer.shooting = player["shooting"]
                    # plPlayer.positioning = player["shooting_attributes"]["positioning"]
                    # plPlayer.definition = player["shooting_attributes"]["definition"]
                    # plPlayer.shot_power = player["shooting_attributes"]["shot_power"]
                    # plPlayer.long_shots = player["shooting_attributes"]["long_shots"]
                    # plPlayer.volleys = player["shooting_attributes"]["volleys"]
                    # plPlayer.penalties = player["shooting_attributes"]["penalties"]
                    # plPlayer.defending = player["defending"]
                    # plPlayer.heading_accuracy = player["defending_attributes"]["heading_accuracy"]
                    # plPlayer.interceptions = player["defending_attributes"]["interceptions"]
                    # plPlayer.sliding_tackle = player["defending_attributes"]["sliding_tackle"]
                    # plPlayer.sliding_tackle = player["defending_attributes"]["standing_tackle"]
                    # plPlayer.dribbling_face = player["dribbling"]
                    # plPlayer.agility = player["dribbling_attributes"]["agility"]
                    # plPlayer.balance = player["dribbling_attributes"]["balance"]
                    # plPlayer.ball_control = player["dribbling_attributes"]["ball_control"]
                    # plPlayer.composure = player["dribbling_attributes"]["composure"]
                    # plPlayer.dribbling = player["dribbling_attributes"]["dribbling"]
                    # plPlayer.reactions = player["dribbling_attributes"]["reactions"]
                    # plPlayer.pace = player["pace"]
                    # plPlayer.acceleration = player["pace_attributes"]["acceleration"]
                    # plPlayer.sprint_speed = player["pace_attributes"]["sprint_speed"]
                    # plPlayer.passing = player["passing"]
                    # plPlayer.crossing = player["passing_attributes"]["crossing"]
                    # plPlayer.curve = player["passing_attributes"]["curve"]
                    # plPlayer.free_kick_accuracy = player["passing_attributes"]["free_kick_accuracy"]
                    # plPlayer.long_passing = player["passing_attributes"]["long_passing"]
                    # plPlayer.short_passing = player["passing_attributes"]["short_passing"]
                    # plPlayer.vision = player["passing_attributes"]["vision"]
                    # plPlayer.physicality = player["physicality"]
                    # plPlayer.aggression = player["physicality_attributes"]["aggression"]
                    # plPlayer.stamina = player["physicality_attributes"]["stamina"]
                    # plPlayer.jumping = player["physicality_attributes"]["jumping"]
                    # plPlayer.strength = player["physicality_attributes"]["strength"]
                    # db.session.add(plPlayer)
                    # db.session.commit()
            
            # striker_stat_weights = {
            #     "sprint_speed": 0.1034,
            #     "finishing": 0.1034,
            #     "dribbling": 0.1034,
            #     "acceleration": 0.1034,
            #     "positioning": 0.086,
            #     "shot_power": 0.086,
            #     "agility": 0.1034,
            #     "strength": 0.0689,
            #     "short_passing": 0.0689,
            #     "balance": 0.0689,
            #     "composure": 0.051,
            #     "jumping": 0.051
            # }
            
            # auba_meta_value = 0
            # for x in auba_meta_stats:
            #     increment = auba_meta_stats[x] * striker_stat_weights[x]
            #     auba_meta_value += increment
            
           # print(ordered_player_list)

            
            #return plPlayer.query.all()
            return(jsonify(response["items"]))    #jsonify
        except:
            print("error ocurred")
            return None


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

if __name__ == "__main__": 
    app.run(host='0.0.0.0')