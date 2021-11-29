from re import M, S
from flask import jsonify
import requests, json
from app import db
import meta_weights

baseUrl = 'https://futdb.app/api/players/search'
apiKey = '97c4dd2b-fe2e-4407-8ea3-f26435d6ce9b'
initial_meta_rating = 1

class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, unique=True)
    rarity = db.Column(db.Integer, nullable=False)
    common_name = db.Column(db.String(80), nullable=True)
    name = db.Column(db.String(80), nullable=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    st_meta_rating = db.Column(db.Integer, nullable=False)
    wing_meta_rating = db.Column(db.Integer, nullable=False)
    cam_meta_rating = db.Column(db.Integer, nullable=False)
    cm_meta_rating = db.Column(db.Integer, nullable=False)
    cdm_meta_rating = db.Column(db.Integer, nullable=False)
    fb_meta_rating = db.Column(db.Integer, nullable=False)
    cb_meta_rating = db.Column(db.Integer, nullable=False)
    nation = db.Column(db.Integer, nullable=True)
    league = db.Column(db.Integer, nullable=True)
    club = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(80), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    attack_work_rate = db.Column(db.String(80), nullable=False)
    defense_work_rate = db.Column(db.String(80), nullable=False)
    foot = db.Column(db.String(80), nullable=False)
    weak_foot = db.Column(db.Integer, nullable=False)
    skill_moves = db.Column(db.Integer, nullable=False)
    shooting = db.Column(db.Integer, nullable=False)
    positioning = db.Column(db.Integer, nullable=False)
    finishing = db.Column(db.Integer, nullable=False)
    shot_power = db.Column(db.Integer, nullable=False)
    long_shots = db.Column(db.Integer, nullable=False)
    volleys = db.Column(db.Integer, nullable=False)
    penalties = db.Column(db.Integer, nullable=False)
    defending = db.Column(db.Integer, nullable=False)
    heading_accuracy = db.Column(db.Integer, nullable=False)
    interceptions = db.Column(db.Integer, nullable=False)
    sliding_tackle = db.Column(db.Integer, nullable=False)
    standing_tackle = db.Column(db.Integer, nullable=False)
    dribbling_face = db.Column(db.Integer, nullable=False)
    agility = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    ball_control = db.Column(db.Integer, nullable=False)
    composure = db.Column(db.Integer, nullable=False)
    dribbling = db.Column(db.Integer, nullable=False)
    reactions = db.Column(db.Integer, nullable=False)
    pace = db.Column(db.Integer, nullable=False)
    acceleration = db.Column(db.Integer, nullable=False)
    sprint_speed = db.Column(db.Integer, nullable=False)
    passing = db.Column(db.Integer, nullable=False)
    crossing = db.Column(db.Integer, nullable=False)
    curve = db.Column(db.Integer, nullable=False)
    free_kick_accuracy = db.Column(db.Integer, nullable=False)
    long_passing = db.Column(db.Integer, nullable=False)
    short_passing = db.Column(db.Integer, nullable=False)
    vision = db.Column(db.Integer, nullable=False)
    physicality = db.Column(db.Integer, nullable=False)
    aggression = db.Column(db.Integer, nullable=False)
    stamina = db.Column(db.Integer, nullable=False)
    jumping = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<id={self.id}, common_name={self.common_name}, rating={self.rating}, st_meta_rating={self.st_meta_rating}>"

    def __init__(self, resource_id, rarity, common_name, name, first_name, last_name, rating, st_meta_rating, wing_meta_rating, cam_meta_rating, cm_meta_rating, cdm_meta_rating, fb_meta_rating, cb_meta_rating, nation, league, club, position, height, weight, attack_work_rate, defense_work_rate, foot, weak_foot, skill_moves, shooting, positioning, finishing, shot_power, long_shots, volleys, penalties, defending, heading_accuracy, interceptions, sliding_tackle, standing_tackle, dribbling_face, agility, balance, ball_control, composure, dribbling, reactions, pace, acceleration, sprint_speed,  passing, crossing, curve, free_kick_accuracy, long_passing, short_passing, vision, physicality, aggression, stamina, jumping, strength):
        #self.id = id
        # 
        self.resource_id = resource_id
        self.rarity = rarity
        self.common_name = common_name
        self.name = name
        self.first_name = first_name
        self.last_name = last_name 
        self.rating = rating
        self.st_meta_rating = st_meta_rating
        self.wing_meta_rating = wing_meta_rating
        self.cam_meta_rating = cam_meta_rating
        self.cm_meta_rating = cm_meta_rating
        self.cdm_meta_rating = cdm_meta_rating
        self.fb_meta_rating = fb_meta_rating
        self.cb_meta_rating = cb_meta_rating
        self.nation = nation
        self.league = league
        self.club = club
        self.position = position
        self.height = height
        self.weight = weight
        self.attack_work_rate = attack_work_rate
        self.defense_work_rate = defense_work_rate
        self.foot = foot
        self.weak_foot = weak_foot
        self.skill_moves = skill_moves
        self.shooting = shooting
        self.positioning = positioning
        self.finishing = finishing
        self.shot_power = shot_power
        self.long_shots = long_shots
        self.volleys = volleys
        self.penalties = penalties
        self.defending = defending
        self.heading_accuracy = heading_accuracy
        self.interceptions = interceptions
        self.standing_tackle = standing_tackle
        self.sliding_tackle = sliding_tackle
        self.dribbling_face = dribbling_face
        self.agility = agility
        self.balance = balance
        self.ball_control = ball_control
        self.composure = composure
        self.dribbling = dribbling
        self.reactions = reactions
        self.pace = pace
        self.acceleration = acceleration
        self.sprint_speed = sprint_speed
        self.passing = passing
        self.crossing = crossing
        self.curve = curve
        self.free_kick_accuracy = free_kick_accuracy
        self.long_passing = long_passing
        self.short_passing = short_passing
        self.vision = vision
        self.physicality = physicality
        self.aggression = aggression
        self.stamina = stamina
        self.jumping = jumping
        self.strength = strength

    @property
    def serialize(self):
        return {
            "id": self.id,
            "resource_id": self.resource_id,
            "rarity": self.rarity,
            "common_name": self.common_name,
            "name": self.name,
            "first_name": self.first_name,
            "last_name": self.name,
            "rating": self.rating,
            "st_meta_rating": self.st_meta_rating,
            "wing_meta_rating": self.wing_meta_rating,
            "cam_meta_rating": self.cam_meta_rating,
            "cm_meta_rating": self.cm_meta_rating,
            "cdm_meta_rating": self.cdm_meta_rating,
            "fb_meta_rating": self.fb_meta_rating,
            "cb_meta_rating": self.cb_meta_rating,
            "nation": self.nation,
            "league" : self.league, 
            "club" : self.club,
            "position" : self.position,
            "height" : self.height,
            "weight" : self.weight,
            "attack_work_rate" : self.attack_work_rate,
            "defense_work_rate" : self.defense_work_rate,
            "foot" : self.foot,
            "weak_foot" : self.weak_foot,
            "skill_moves" : self.skill_moves,
            "shooting" : self.shooting,
            "positioning" : self.positioning,
            "finishing" : self.finishing,
            "shot_power" : self.shot_power,
            "long_shots" : self.long_shots,
            "volleys" : self.volleys,
            "penalties" : self.penalties,
            "defending" : self.defending,
            "heading_accuracy" : self.heading_accuracy,
            "interceptions" : self.interceptions,
            "sliding_tackle" : self.sliding_tackle,
            "standing_tackle" : self.standing_tackle,
            "dribbling_face" : self.dribbling_face,
            "agility" : self.agility,
            "balance" : self.balance,
            "ball_control" : self.ball_control,
            "composure" : self.composure,
            "dribbling" : self.dribbling,
            "reactions" : self.reactions,
            "pace" : self.pace,
            "acceleration" : self.acceleration,
            "sprint_speed" : self.sprint_speed,
            "passing" : self.passing,
            "crossing" : self.crossing,
            "curve" : self.curve,
            "free_kick_accuracy" : self.free_kick_accuracy,
            "long_passing" : self.long_passing,
            "short_passing" : self.short_passing,
            "vision" : self.vision,
            "physicality" : self.physicality,
            "aggression" : self.aggression,
            "stamina" : self.stamina,
            "jumping" : self.jumping,
            "strength" : self.strength
        }

#ask how to avoid repetitions
def getsquad(league):
    squad = { 
        'formation': '4231',
        'LW': Player.query.filter_by(**{'league' : league}).filter_by(**{'position' : 'LW'}).order_by(Player.wing_meta_rating.desc()).first().serialize,
        'ST': Player.query.filter_by(**{'league' : league}).order_by(Player.st_meta_rating.desc()).first().serialize,
        'RW': Player.query.filter_by(**{'league' : league}).filter_by(**{'position' : 'RW'}).order_by(Player.wing_meta_rating.desc()).first().serialize,
        'CAM': Player.query.filter_by(**{'league' : league}).order_by(Player.cam_meta_rating.desc()).first().serialize,
        'CM': Player.query.filter_by(**{'league' : league}).order_by(Player.cm_meta_rating.desc()).first().serialize,
        'CDM': Player.query.filter_by(**{'league' : league}).order_by(Player.cdm_meta_rating.desc()).first().serialize,
        'LB': Player.query.filter_by(**{'league' : league}).filter_by(**{'position' : 'LB'}).order_by(Player.fb_meta_rating.desc()).first().serialize,
        'CB1': Player.query.filter_by(**{'league' : league}).order_by(Player.cb_meta_rating.desc()).first().serialize,
        'CB2': Player.query.filter_by(**{'league' : league}).order_by(Player.cb_meta_rating.desc()).offset(1).first().serialize,
        'RB': Player.query.filter_by(**{'league' : league}).filter_by(**{'position' : 'RB'}).order_by(Player.fb_meta_rating.desc()).first().serialize,
        }
    print((squad))
    return squad

def getstrikers(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.st_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def getwingers(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.wing_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def getcams(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.cam_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def getcms(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.cm_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def getcdms(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.cdm_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def getfbs(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.fb_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def getcbs(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.cb_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data



# def getplstrikers():
#     meta_rating_list = Player.query.order_by(Player.st_meta_rating.desc()).limit(10).all()
#     #map(lambda player: print(player.serialize()), meta_rating_list)
#     data = jsonify(data=[i.serialize for i in meta_rating_list])
#     #return jsonify(meta_rating_list)
#     return data

def showmeta():
    print(meta_weights.st["finishing"])
    data = meta_weights.st["finishing"]
    return jsonify(str(data))

#calculate meta stats for every player in every position
def get_meta_ratings():
    get_st_meta()
    get_wing_meta()
    get_cam_meta()
    get_cm_meta()
    get_cdm_meta()
    get_fb_meta()
    get_cb_meta()
    return 'Meta ratings calculated'

def get_st_meta():
    st_meta = meta_weights.st
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        st_meta_rating = (player.sprint_speed * st_meta["sprint_speed"] + player.acceleration * st_meta["acceleration"]
            + player.finishing * st_meta["finishing"] + player.positioning * st_meta["positioning"] + player.shot_power * st_meta["shot_power"]
            + player.short_passing * st_meta["short_passing"]
            + player.dribbling * st_meta["dribbling"] + player.reactions * st_meta["reactions"] + player.agility * st_meta["agility"]
            + player.ball_control * st_meta["ball_control"] + player.composure * st_meta["composure"]
            + player.strength * st_meta["strength"] + player.jumping * st_meta["jumping"])
             
        player.st_meta_rating = st_meta_rating
        db.session.commit()
    return None

def get_wing_meta():
    wing_meta = meta_weights.wing
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        wing_meta_rating = (player.sprint_speed * wing_meta["sprint_speed"] + player.finishing * wing_meta["finishing"]
            + player.dribbling * wing_meta["dribbling"] + player.acceleration * wing_meta["acceleration"]
            + player.positioning * wing_meta["positioning"] + player.shot_power * wing_meta["shot_power"]
            + player.agility * wing_meta["agility"] + player.vision * wing_meta["vision"]
            + player.crossing * wing_meta["crossing"] + player.short_passing * wing_meta["short_passing"]
            + player.balance * wing_meta["balance"] + player.composure * wing_meta["stamina"] + player.jumping * wing_meta["stamina"])
        
        player.wing_meta_rating = wing_meta_rating
        db.session.commit()
    return None

def get_cam_meta():
    cam_meta = meta_weights.cam
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        cam_meta_rating = (player.sprint_speed * cam_meta["sprint_speed"] + player.finishing * cam_meta["finishing"]
            + player.dribbling * cam_meta["dribbling"] + player.acceleration * cam_meta["acceleration"]
            + player.positioning * cam_meta["positioning"] + player.shot_power * cam_meta["shot_power"] + player.long_shots * cam_meta["long_shots"]
            + player.agility * cam_meta["agility"]
            + player.strength * cam_meta["strength"] + player.short_passing * cam_meta["short_passing"] + player.long_passing * cam_meta["long_passing"]
            + player.balance * cam_meta["balance"] + player.composure * cam_meta["composure"] + player.vision * cam_meta["vision"] 
            + player.stamina * cam_meta["stamina"])

        player.cam_meta_rating = cam_meta_rating
        db.session.commit()
    return None

def get_cm_meta():
    cm_meta = meta_weights.cm
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        cm_meta_rating = (player.sprint_speed * cm_meta["sprint_speed"] + player.acceleration * cm_meta["acceleration"] 
            + player.finishing * cm_meta["finishing"] + player.long_shots * cm_meta["long_shots"] + player.reactions * cm_meta["reactions"]
            + player.agility * cm_meta["agility"] + player.balance * cm_meta["balance"]
            + player.long_passing * cm_meta["long_passing"] + player.short_passing * cm_meta["short_passing"] + player.vision * cm_meta["vision"]
            + player.strength * cm_meta["strength"] + player.stamina * cm_meta["stamina"] + player.jumping * cm_meta["jumping"])

        cm_meta_rating += player.weak_foot * 1
        cm_meta_rating += player.skill_moves * 0.75
        if player.attack_work_rate == "high": cm_meta_rating += 3
        elif player.attack_work_rate == "med": cm_meta_rating += 1
        if player.defense_work_rate == "high": cm_meta_rating += 3
        elif player.defense_work_rate == "med": cm_meta_rating += 1

        player.cm_meta_rating = cm_meta_rating
        db.session.commit()
       
    return None

def get_cdm_meta():
    cdm_meta = meta_weights.cdm
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        cdm_meta_rating = (player.sprint_speed * cdm_meta["sprint_speed"]
            + player.long_passing * cdm_meta["long_passing"] + player.acceleration * cdm_meta["acceleration"]
            + player.strength * cdm_meta["strength"] + player.short_passing * cdm_meta["short_passing"]
            + player.balance * cdm_meta["balance"] + player.dribbling * cdm_meta["dribbling"] + player.jumping * cdm_meta["jumping"]
            + player.interceptions * cdm_meta["interceptions"] + player.standing_tackle * cdm_meta["standing_tackle"] + 
            + player.aggression * cdm_meta["aggression"])
        
        cdm_meta_rating += player.weak_foot * 1
        if player.attack_work_rate == "high": cdm_meta_rating += 3
        elif player.attack_work_rate == "med": cdm_meta_rating += 1
        if player.defense_work_rate == "high": cdm_meta_rating += 3
        elif player.defense_work_rate == "med": cdm_meta_rating += 1

        player.cdm_meta_rating = cdm_meta_rating
        db.session.commit()
    return None

def get_fb_meta():
    fb_meta = meta_weights.fb
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        fb_meta_rating = (player.sprint_speed * fb_meta["sprint_speed"] + player.acceleration * fb_meta["acceleration"]
            + player.interceptions * fb_meta["interceptions"] + player.standing_tackle * fb_meta["standing_tackle"]
            + player.dribbling * fb_meta["dribbling"] + player.agility * fb_meta["agility"] + player.balance * fb_meta["balance"]
            + player.short_passing * fb_meta["short_passing"] + player.long_passing * fb_meta["long_passing"]  + player.vision * fb_meta["vision"]
            + player.strength * fb_meta["strength"] + player.stamina * fb_meta["stamina"])
            

        player.fb_meta_rating = fb_meta_rating
        db.session.commit()
    return None

def get_cb_meta():
    cb_meta = meta_weights.cb
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        cb_meta_rating = (player.sprint_speed * cb_meta["sprint_speed"] + player.acceleration * cb_meta["acceleration"]
            + player.agility * cb_meta["agility"] + player.reactions * cb_meta["reactions"]
             + player.short_passing * cb_meta["short_passing"] + player.long_passing * cb_meta["long_passing"]
            + player.composure * cb_meta["composure"] + player.jumping * cb_meta["jumping"] + player.aggression * cb_meta["aggression"] + player.strength * cb_meta["strength"]
            + player.interceptions * cb_meta["interceptions"] + player.sliding_tackle * cb_meta["sliding_tackle"] + player.standing_tackle * cb_meta["standing_tackle"]) 

        cb_meta_rating += player.height * 0.01
        if player.attack_work_rate == "low": cb_meta_rating += 3
        elif player.attack_work_rate == "med": cb_meta_rating += 1
        if player.defense_work_rate == "high": cb_meta_rating += 3
        elif player.defense_work_rate == "med": cb_meta_rating += 1

        player.cb_meta_rating = cb_meta_rating
        db.session.commit()
    return None

def request_players_by_league():
    leagues = [13, 16, 19, 31, 53] # 13: PL, 16:Ligue1, 19: Bundes, 31:SerieA, 53: LaLiga
    for league in leagues:
        print(league)
        request_data = { 
            "rarity": 1,
            "league": league 
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'X-AUTH-TOKEN': '{}'.format(apiKey)
        }
        try:
            responsePageTotalHearer = requests.post('https://futdb.app/api/players/search', json=request_data, headers=headers).json()
            
            for page in range(1, responsePageTotalHearer["page_total"], 1):
                page_response = requests.post(baseUrl+'?page='+str(page), json=request_data, headers=headers).json()
                for player in page_response["items"]:
                    print(player["common_name"], player["foot"], player["height"], player["position"], player["defending_attributes"]["interceptions"])
                    PlayerItem = Player(
                        player["resource_id"], 
                        player["rarity"],
                        player["common_name"],
                        player["name"],
                        player["first_name"],
                        player["last_name"],
                        player["rating"],
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        player["nation"],
                        player["league"],
                        player["club"],
                        player["position"],
                        player["height"],
                        player["weight"],
                        player["attack_work_rate"],
                        player["defense_work_rate"],
                        player["foot"],
                        player["weak_foot"],
                        player["skill_moves"],
                        player["shooting"],
                        player["shooting_attributes"]["positioning"],
                        player["shooting_attributes"]["finishing"],
                        player["shooting_attributes"]["shot_power"],
                        player["shooting_attributes"]["long_shots"],
                        player["shooting_attributes"]["volleys"],
                        player["shooting_attributes"]["penalties"],  
                        player["defending"],
                        player["defending_attributes"]["heading_accuracy"],
                        player["defending_attributes"]["interceptions"],
                        player["defending_attributes"]["sliding_tackle"],
                        player["defending_attributes"]["standing_tackle"],
                        player["dribbling"],                
                        player["dribbling_attributes"]["agility"],
                        player["dribbling_attributes"]["balance"],
                        player["dribbling_attributes"]["ball_control"],
                        player["dribbling_attributes"]["composure"],
                        player["dribbling_attributes"]["dribbling"],
                        player["dribbling_attributes"]["reactions"],
                        player["pace"],   
                        player["pace_attributes"]["acceleration"],
                        player["pace_attributes"]["sprint_speed"],
                        player["passing"],  
                        player["passing_attributes"]["crossing"],
                        player["passing_attributes"]["curve"],
                        player["passing_attributes"]["free_kick_accuracy"],
                        player["passing_attributes"]["long_passing"],
                        player["passing_attributes"]["short_passing"],
                        player["passing_attributes"]["vision"],
                        player["physicality"],
                        player["physicality_attributes"]["aggression"],
                        player["physicality_attributes"]["stamina"],
                        player["physicality_attributes"]["jumping"],
                        player["physicality_attributes"]["strength"]
                    )  
                    db.session.add(PlayerItem)
                    db.session.commit()
            #return(jsonify(response["items"]))  #meanwhile jsonifying page 1 of the items in the first response
            
        except:
            print("error ocurred")
            return None
    return '<div><h3>Player database updated:</h3><ul><li>Premier League</li><li>Ligue 1</li><li>Bundesliga</li><li>SerieA</li><li>LaLiga</li></ul></div>'

if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()
    print("Done!")