from flask import jsonify
import requests
from app import db

baseUrl = 'https://futdb.app/api/players/search'
apiKey = '97c4dd2b-fe2e-4407-8ea3-f26435d6ce9b'

class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(80), nullable=False)
    # common_name = db.Column(db.String(80), unique=True, nullable=False)
    # first_name = db.Column(db.String(80), nullable=False)
    # last_name = db.Column(db.String(80), nullable=False)
    # rarity = db.Column(db.Integer, nullable=False)
    # rating = db.Column(db.Integer, nullable=False)
    # nation = db.Column(db.Integer, nullable=False)
    # league = db.Column(db.Integer, nullable=False)
    # position = db.Column(db.String(80), nullable=False)
    # club = db.Column(db.Integer, nullable=False)
    # foot = db.Column(db.String(80), nullable=False)
    # meta_value = db.Column(db.Integer, nullable=False)
    # height = db.Column(db.Integer, nullable=False)
    # weigth = db.Column(db.Integer, nullable=False)
    # attack_work_rate = db.Column(db.String(80), nullable=False)
    # defense_work_rate = db.Column(db.String(80), nullable=False)
    # weak_foot = db.Column(db.Integer, nullable=False)
    # skill_moves = db.Column(db.Integer, nullable=False)
    shooting = db.Column(db.Integer, nullable=False)
    # positioning = db.Column(db.Integer, nullable=False)
    # definition = db.Column(db.Integer, nullable=False)
    # shot_power = db.Column(db.Integer, nullable=False)
    # long_shots = db.Column(db.Integer, nullable=False)
    # volleys = db.Column(db.Integer, nullable=False)
    # penalties = db.Column(db.Integer, nullable=False)
    # defending = db.Column(db.Integer, nullable=False)
    # heading_accuracy = db.Column(db.Integer, nullable=False)
    # interceptions = db.Column(db.Integer, nullable=False)
    # sliding_tackle = db.Column(db.Integer, nullable=False)
    # standing_tackle = db.Column(db.Integer, nullable=False)
    # dribbling_face = db.Column(db.Integer, nullable=False)
    # agility = db.Column(db.Integer, nullable=False)
    # balance = db.Column(db.Integer, nullable=False)
    # ball_control = db.Column(db.Integer, nullable=False)
    # composure = db.Column(db.Integer, nullable=False)
    # dribbling = db.Column(db.Integer, nullable=False)
    # reactions = db.Column(db.Integer, nullable=False)
    # pace = db.Column(db.Integer, nullable=False)
    # acceleration = db.Column(db.Integer, nullable=False)
    # sprint_speed = db.Column(db.Integer, nullable=False)
    # passing = db.Column(db.Integer, nullable=False)
    # crossing = db.Column(db.Integer, nullable=False)
    # curve = db.Column(db.Integer, nullable=False)
    # free_kick_accuracy = db.Column(db.Integer, nullable=False)
    # long_passing = db.Column(db.Integer, nullable=False)
    # short_passing = db.Column(db.Integer, nullable=False)
    # vision = db.Column(db.Integer, nullable=False)
    # physicality = db.Column(db.Integer, nullable=False)
    # aggression = db.Column(db.Integer, nullable=False)
    # stamina = db.Column(db.Integer, nullable=False)
    # jumping = db.Column(db.Integer, nullable=False)
    # strength = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<id={self.id}, name={self.name}, shooting={self.shooting}>"

    def __init__(self, resource_id, name, shooting):
        self.resource_id= resource_id
        self.name = name
        self.shooting = shooting

    def serialize(self):
        return {
            "id": self.id,
            "resource_id": self.resource_id,
            "name": self.name,
            # "common_name": self.common_name,
            # "first_name": self.first_name,
            # "last_name": self.last_name,
            # "rarity": self.rarity,
            # "rating": self.rating,
            # "nation": self.nation,
            # "league" : self.league, 
            # "position" : self.position,
            # "club" : self.club,
            # "foot" : self.foot, 
            # "meta_value" : self.meta_value,
            # "height" : self.height,
            # "weigth" : self.weigth,
            # "attack_work_rate" : self.attack_work_rate,
            # "defense_work_rate" : self.defense_work_rate,
            # "weak_foot" : self.weak_foot,
            # "skill_moves" : self.skill_moves,
            "shooting" : self.shooting
            # "positioning" : self.positioning,
            # "definition" : self.definition
            # "shot_power" : self.shot_power,
            # "long_shots" : self.long_shots,
            # "volleys" : self.volleys,
            # "penalties" : self.penalties,
            # "defending" : self.defending,
            # "heading_accuracy" : self.heading_accuracy,
            # "interceptions" : self.interceptions,
            # "sliding_tackle" : self.sliding_tackle,
            # "standing_tackle" : self.standing_tackle,
            # "dribbling_face" : self.dribbling_face,
            # "agility" : self.agility,
            # "balance" : self.balance,
            # "ball_control" : self.ball_control,
            # "composure" : self.composure,
            # "dribbling" : self.dribbling,
            # "reactions" : self.reactions,
            # "pace" : self.pace,
            # "acceleration" : self.acceleration,
            # "sprint_speed" : self.sprint_speed,
            # "passing" : self.passing,
            # "crossing" : self.crossing,
            # "curve" : self.curve,
            # "free_kick_accuracy" : self.free_kick_accuracy,
            # "long_passing" : self.long_passing,
            # "short_passing" : self.short_passing,
            # "vision" : self.vision,
            # "physicality" : self.physicality,
            # "aggression" : self.aggression,
            # "stamina" : self.stamina,
            # "jumping" : self.jumping,
            # "strength" : self.strength
        }

def getplplayer(resource_id):
    player = Player.query.get(resource_id)
    print(player)
    return 'hello getplplayer'

def getplList():
    # player_list = Player.query.order_by(Player.shooting.amount.desc())
    # print(type(player_list))
    # print(player_list)
    player_list = Player.query.order_by(Player.shooting.desc()).all()
    print(player_list)
    return 'hello player list'

def request_players_by_league():
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
            
            #Player.query.delete()
        
            response = requests.post('https://futdb.app/api/players/search', json=request_data, headers=headers).json()
            
            for page in range(1, response["page_total"], 1):
                response2 = requests.post(baseUrl+'?page='+str(page), json=request_data, headers=headers).json()
                #print(response["items"])
                for player in response2["items"]:
                    print(player["id"], player["name"])
                    plPlayer = Player(player["resource_id"], player["name"], player["shooting"])
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
                    db.session.add(plPlayer)
                    db.session.commit()
            
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
            return(jsonify(response["items"]))  #meanwhile jsonifying page 1 of the items in the first response
        except:
            print("error ocurred")
            return None

    

if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()
    print("Done!")