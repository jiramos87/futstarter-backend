from re import M, S
from flask import jsonify, request, abort
import requests, json
from app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from requests.api import head
from app import db
import meta_weights
import formations
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from base64 import b64encode
import base64

baseUrl = 'https://futdb.app/api/players/search'
initial_meta_rating = 1
apiKey = '97c4dd2b-fe2e-4407-8ea3-f26435d6ce9b'
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(512))
    is_admin = db.Column(db.Boolean, nullable=False, default=0)

    def __init__(self, username, email, password, is_admin):
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_admin": self.is_admin,
            "password": self.password
        }

class Squad(db.Model):
    __tablename__ = 'squad'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    global_id = db.Column(db.Integer, unique=True)
    squad_name = db.Column(db.String(100), unique=False)
    username = db.Column(db.String(20), unique=False)
    formation = db.Column(db.String(10), unique=False)
    squad_dict = db.Column(db.String(1000), unique=False)

    def __init__(self, global_id, squad_name, username, formation, squad_dict):
        
        self.global_id = global_id
        self.squad_name = squad_name
        self.username = username
        self.formation = formation
        self.squad_dict = squad_dict
    
    def serialize(self):
        return {
            "id": self.id,
            "global_id": self.global_id,
            "squad_name": self.squad_name,
            "username": self.username,
            "formation": self.formation,
            "squad_dict": self.squad_dict
        }
class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    global_id = db.Column(db.Integer, nullable=False)
    rarity = db.Column(db.Integer, nullable=False)
    common_name = db.Column(db.String(80), nullable=True)
    name = db.Column(db.String(80), nullable=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    lw_meta_rating = db.Column(db.Integer, nullable=False)
    lf_meta_rating = db.Column(db.Integer, nullable=False)
    lm_meta_rating = db.Column(db.Integer, nullable=False)
    lst_meta_rating = db.Column(db.Integer, nullable=False)
    cst_meta_rating = db.Column(db.Integer, nullable=False)
    rst_meta_rating = db.Column(db.Integer, nullable=False)
    cf_meta_rating = db.Column(db.Integer, nullable=False)
    rw_meta_rating = db.Column(db.Integer, nullable=False)
    rf_meta_rating = db.Column(db.Integer, nullable=False)
    rm_meta_rating = db.Column(db.Integer, nullable=False)
    lcam_meta_rating = db.Column(db.Integer, nullable=False)
    ccam_meta_rating = db.Column(db.Integer, nullable=False)
    rcam_meta_rating = db.Column(db.Integer, nullable=False)
    lcm_meta_rating = db.Column(db.Integer, nullable=False)
    ccm_meta_rating = db.Column(db.Integer, nullable=False)
    rcm_meta_rating = db.Column(db.Integer, nullable=False)
    lcdm_meta_rating = db.Column(db.Integer, nullable=False)
    ccdm_meta_rating = db.Column(db.Integer, nullable=False)
    rcdm_meta_rating = db.Column(db.Integer, nullable=False)
    lwb_meta_rating = db.Column(db.Integer, nullable=False)
    lb_meta_rating = db.Column(db.Integer, nullable=False)
    lcb_meta_rating = db.Column(db.Integer, nullable=False)
    ccb_meta_rating = db.Column(db.Integer, nullable=False)
    rcb_meta_rating = db.Column(db.Integer, nullable=False)
    rwb_meta_rating = db.Column(db.Integer, nullable=False)
    rb_meta_rating = db.Column(db.Integer, nullable=False)
    gk_meta_rating = db.Column(db.Integer, nullable=False)
    nation = db.Column(db.Integer, nullable=True)
    nation_str = db.Column(db.String(80), nullable=True)
    league = db.Column(db.Integer, nullable=True)
    league_str = db.Column(db.String(80), nullable=True)
    club = db.Column(db.Integer, nullable=True)
    club_str = db.Column(db.String(80), nullable=True)
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
    diving = db.Column(db.Integer, nullable=True)
    handling = db.Column(db.Integer, nullable=True)
    kicking = db.Column(db.Integer, nullable=True)
    gk_positioning = db.Column(db.Integer, nullable=True)
    reflexes = db.Column(db.Integer, nullable=True)
    # price_playstation = db.Column(db.BigInteger, nullable=True)
    # price_xbox = db.Column(db.BigInteger, nullable=True)
    # price_pc = db.Column(db.BigInteger, nullable=True)

    def __repr__(self):
        return f"<id={self.global_id}, common_name={self.common_name}, rating={self.rating}>"

    def __init__(self, global_id, rarity, common_name, name, first_name, last_name, age, rating, lw_meta_rating, lf_meta_rating, lm_meta_rating, lst_meta_rating, cst_meta_rating, rst_meta_rating, cf_meta_rating, rw_meta_rating, rf_meta_rating, rm_meta_rating, lcam_meta_rating, ccam_meta_rating, rcam_meta_rating, lcm_meta_rating, ccm_meta_rating, rcm_meta_rating, lcdm_meta_rating, ccdm_meta_rating, rcdm_meta_rating, lwb_meta_rating, lb_meta_rating, lcb_meta_rating, ccb_meta_rating, rcb_meta_rating, rwb_meta_rating, rb_meta_rating, gk_meta_rating, nation, nation_str, league, league_str, club, club_str, position, height, weight, attack_work_rate, defense_work_rate, foot, weak_foot, skill_moves, shooting, positioning, finishing, shot_power, long_shots, volleys, penalties, defending, heading_accuracy, interceptions, sliding_tackle, standing_tackle, dribbling_face, agility, balance, ball_control, composure, dribbling, reactions, pace, acceleration, sprint_speed,  passing, crossing, curve, free_kick_accuracy, long_passing, short_passing, vision, physicality, aggression, stamina, jumping, strength, diving, handling, kicking, gk_positioning, reflexes):
        #self.id = id
        # 
        self.global_id = global_id
        self.rarity = rarity
        self.common_name = common_name
        self.name = name
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age
        self.rating = rating
        self.lw_meta_rating = lw_meta_rating
        self.lf_meta_rating = lf_meta_rating
        self.lm_meta_rating = lm_meta_rating
        self.lst_meta_rating = lst_meta_rating
        self.cst_meta_rating = cst_meta_rating
        self.rst_meta_rating = rst_meta_rating
        self.cf_meta_rating = cf_meta_rating
        self.rw_meta_rating = rw_meta_rating
        self.rf_meta_rating = rf_meta_rating
        self.rm_meta_rating = rm_meta_rating
        self.lcam_meta_rating = lcam_meta_rating
        self.ccam_meta_rating = ccam_meta_rating
        self.rcam_meta_rating = rcam_meta_rating
        self.lcm_meta_rating = lcm_meta_rating
        self.ccm_meta_rating = ccm_meta_rating
        self.rcm_meta_rating = rcm_meta_rating
        self.lcdm_meta_rating = lcdm_meta_rating
        self.ccdm_meta_rating = ccdm_meta_rating
        self.rcdm_meta_rating = rcdm_meta_rating
        self.lwb_meta_rating = lwb_meta_rating
        self.lb_meta_rating = lb_meta_rating
        self.lcb_meta_rating = lcb_meta_rating
        self.ccb_meta_rating = ccb_meta_rating
        self.rcb_meta_rating = rcb_meta_rating
        self.rwb_meta_rating = rwb_meta_rating
        self.rb_meta_rating = rb_meta_rating
        self.gk_meta_rating = gk_meta_rating
        self.nation = nation
        self.nation_str = nation_str
        self.league = league
        self.league_str = league_str
        self.club = club
        self.club_str = club_str
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
        self.diving = diving
        self.handling = handling
        self.kicking = kicking
        self.gk_positioning = gk_positioning
        self.reflexes = reflexes 
        # self.price_playstation = price_playstation
        # self.price_xbox = price_xbox
        # self.price_pc = price_pc
    
    @property
    def serialize(self):
        return {
            "id": self.id,
            "global_id": self.global_id,
            "rarity": self.rarity,
            "common_name": self.common_name,
            "name": self.name,
            "first_name": self.first_name,
            "last_name": self.name,
            "age": self.age,
            "rating": self.rating,
            "lw_meta_rating": self.lw_meta_rating,
            "lf_meta_rating": self.lf_meta_rating,
            "lm_meta_rating": self.lm_meta_rating,
            "lst_meta_rating": self.lst_meta_rating,
            "cst_meta_rating": self.cst_meta_rating,
            "rst_meta_rating": self.rst_meta_rating,
            "cf_meta_rating": self.cf_meta_rating,
            "rw_meta_rating": self.rw_meta_rating,
            "rf_meta_rating": self.rf_meta_rating,
            "rm_meta_rating": self.rm_meta_rating,
            "lcam_meta_rating": self.lcam_meta_rating,
            "ccam_meta_rating": self.ccam_meta_rating,
            "rcam_meta_rating": self.rcam_meta_rating,
            "lcm_meta_rating": self.lcm_meta_rating,
            "ccm_meta_rating": self.ccm_meta_rating,
            "rcm_meta_rating": self.rcm_meta_rating,
            "lcdm_meta_rating": self.lcdm_meta_rating,
            "ccdm_meta_rating": self.ccdm_meta_rating,
            "rcdm_meta_rating": self.rcdm_meta_rating,
            "lwb_meta_rating": self.lwb_meta_rating,
            "lb_meta_rating": self.lb_meta_rating,
            "lcb_meta_rating": self.lcb_meta_rating,
            "ccb_meta_rating": self.ccb_meta_rating,
            "rcb_meta_rating": self.rcb_meta_rating,
            "rwb_meta_rating": self.rwb_meta_rating,
            "rb_meta_rating": self.rb_meta_rating,
            "gk_meta_rating": self.gk_meta_rating,
            "nation": self.nation,
            "nation_str": self.nation_str,
            "league" : self.league, 
            "league_str": self.league_str,
            "club" : self.club,
            "club_str": self.club_str,
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
            "strength" : self.strength,
            "diving": self.diving,
            "handling": self.handling,
            "kicking": self.kicking,
            "gk_positioning": self.gk_positioning,
            "reflexes": self.reflexes
            # "price_playstation": self.price_playstation,
            # "price_xbox": self.price_xbox,
            # "price_pc": self.price_pc
        }

##################################  USER METHODS

def register(request_body):
    if request.method == 'POST':
        db.session.add(User(is_admin=0, username=request_body['username'], email=request_body['email'], password=bcrypt.generate_password_hash(request_body['password']).decode('utf-8')))
        db.session.commit()
        users = User.query.all()
        serialized_users = map(lambda user: user.serialize(), users)
        filtered_users = list(filter(lambda user: user['username'] == request_body['username'], serialized_users))
        access_token = create_access_token(identity=filtered_users[0]['username'])
        if(filtered_users.count != 0 or filtered_users != []):
            return {"user": list(filtered_users), "status": 200, "token": access_token}
    

def login(request_body):
    print('backend login obj', request_body)
    users = User.query.all()
    serialized_users = map(lambda user: user.serialize(), users)
    filtered_users = list(filter(lambda user: user['username'] == request_body['username'], serialized_users))
    print('filtered users', filtered_users)
    #print(filtered_users, bcrypt.generate_password_hash(request_body['password']))
    if(filtered_users.count == 0 or filtered_users == []):
        return {"status": 401, "message": "Incorrect username or password"}
    elif(bcrypt.check_password_hash(filtered_users[0]['password'], request_body['password'])):
        access_token = create_access_token(identity=filtered_users[0]['username'])
        return {"user": list(filtered_users),"token": access_token, "status": 200}
    else:
        return abort(401)

def search_players(search_string):
    if len(search_string) >= 3:
        players = Player.query.filter(Player.last_name.contains(search_string) | Player.first_name.contains(search_string)).limit(10)
        serialized_players = map(lambda player: player.serialize, players)
        filtered_players = list(serialized_players)
        if filtered_players.count == 0:
            return {"status": 400, "message": "No players found"}
        else:
            return {"status": 200, "result": filtered_players}
    else: 
        return {"status": 400, "message": "query too short"}

def get_player_by_id(global_id):
    if global_id != 0:
        player = Player.query.filter(Player.global_id == global_id).first()
        serialized_player = player.serialize
        filtered_player = list(serialized_player)
        if filtered_player.count == 0:
            return {"status": 400, "message": "No players found"}
        else:
            return {"status": 200, "result": serialized_player}
    else:
        return {"status": 400, "result": None}

def get_player_price(player_global_id):
    headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'X-AUTH-TOKEN': '{}'.format(apiKey)
        }
    price_res = requests.get('https://futdb.app/api/players/'+str(player_global_id)+'/price', headers=headers).json()
    price_ps = price_res["playstation"]["price"]
 
    return {"status": 200, "price": price_ps}

def save_squad(req_body, current_user):
    #print(req_body)
    squads_count = Squad.query.count()  
    global_id = squads_count + 1
    squad_list = req_body['squad_data']
    print(squad_list)
    db.session.add(Squad(global_id, req_body['squad_name'], current_user, req_body['formation'], str(squad_list)))
    db.session.commit()
    return {"message": "squad saved", "status": 200}

def get_user_squads(current_user):
    print('hello get squads')
    squads = Squad.query.all()
    serialized_squads = map(lambda squad: squad.serialize(), squads)
    filtered_squads = list(filter(lambda squad: squad['username'] == current_user, serialized_squads))
    # squads_data = []
    # for squad in filtered_squads:
    #     print(squad['squad_dict'][0])
    #     squad_data = get_squad_from_global_ids(squad['formation'], squad['squad_name'], json.loads(squad['squad_dict']))
    #     squads_data.append(squad_data) 
    # print(squads_data)
    return {"squads_data": filtered_squads, "status": 200}

def get_squad_from_global_ids(squad_formation, squad_name, global_id_list):
    print(global_id_list)
    players_data = []
    players = Player.query.all()
    serialized_players = map(lambda player: player.serialize, players)

    for i in range(11):
        print('index', i, 'global_id', global_id_list[i])
        if global_id_list[i] == 0:
            players_data.append(None)
        else:
            filtered_player = list(filter(lambda player: player['global_id'] == global_id_list[i], serialized_players))
            print(filtered_player)
            players_data.append(filtered_player)
            
    squad_data = {
        "formation": squad_formation, 
        "squad_name": squad_name,
        "players_data": players_data
    }
    return squad_data

def load_squad(squad, current_user):   
    return None

def delete_squad(user_squad, current_user): 
    return None

def delete_all_squads(squad_id):
    db.session.query(Squad).filter(Squad.id==squad_id).delete() 
    db.session.commit()

    return 'user squads deleted'

    #########################  ADMIN METHODS

def filter_players(filter_body):
    print(filter_body)
    filter_result = Player.query.filter_by().all()
    print(filter_result)
    if filter_result.count == 0:
        return {"status": 400, "message": "No players found", "data": None}
    else:
        for key, value in filter_result.items():
            print(value.serialize)
            filter_result[key] = value.serialize
        data = {"status": 200, "result": filter_result}
        print(data)
        return data
   
def delete_user(user_id):
    user = User.query.get(user_id)
    print(user)
    db.session.delete(user)
    db.session.commit()
    return 'User deleted'

def make_admin(username):
    user = User.query.filter_by(username=username)
    user.is_admin = 1   
    db.session.commit()
    return { 
        "message": 'User is now admin', 
        "status": 200
    }
    
def update():
    update_player_db()
    calculate_meta()
    return 'Database initialized'

def update_player_db():
    ## MISSING: if database is populated, erase
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

                    nation_res = requests.get('https://futdb.app/api/nations/'+str(player["nation"]), headers=headers).json()
                    league_res = requests.get('https://futdb.app/api/leagues/'+str(player["league"]), headers=headers).json()
                    club_res = requests.get('https://futdb.app/api/clubs/'+str(player["club"]), headers=headers).json()
                    #price_res = requests.get('https://futdb.app/api/players/'+str(player["id"])+'/price', headers=headers).json()

                    nation_res_name = nation_res["item"]["name"]
                    league_res_name = league_res["item"]["name"]
                    club_res_name = club_res["item"]["name"]
                    # price_res_playstation = price_res["playstation"]["price"]
                    # price_res_xbox = price_res["xbox"]["price"]
                    # price_res_pc = price_res["pc"]["price"]
                    
                    
                    print(player["id"], player["common_name"])
                    PlayerItem = Player(
                        player["id"], 
                        player["rarity"],
                        player["common_name"],
                        player["name"],
                        player["first_name"],
                        player["last_name"],
                        player["age"],
                        player["rating"],
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        initial_meta_rating,
                        player["nation"],
                        nation_res_name,
                        player["league"],
                        league_res_name,
                        player["club"],
                        club_res_name,
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
                        player["physicality_attributes"]["strength"],
                        player["goalkeeper_attributes"]["diving"] if player["goalkeeper_attributes"]["diving"] != None else 0,
                        player["goalkeeper_attributes"]["handling"] if player["goalkeeper_attributes"]["handling"] != None else 0, 
                        player["goalkeeper_attributes"]["kicking"] if player["goalkeeper_attributes"]["kicking"] != None else 0,
                        player["goalkeeper_attributes"]["positioning"] if player["goalkeeper_attributes"]["positioning"] != None else 0,
                        player["goalkeeper_attributes"]["reflexes"] if player["goalkeeper_attributes"]["reflexes"] != None else 0
                    )  
                    db.session.add(PlayerItem)
                    db.session.commit()
            #return(jsonify(response["items"]))  #meanwhile jsonifying page 1 of the items in the first response
            
        except:
            print("error ocurred")
            return None
    return '<div><h3>Player database updated:</h3><ul><li>Premier League</li><li>Ligue 1</li><li>Bundesliga</li><li>SerieA</li><li>LaLiga</li></ul></div>'

def calculate_meta():
    get_lw_meta()
    get_lf_meta()
    get_lm_meta()
    get_lst_meta()
    get_cst_meta()
    get_rst_meta()
    get_cf_meta()
    get_rw_meta()
    get_rf_meta()
    get_rm_meta()
    get_lcam_meta()
    get_ccam_meta()
    get_rcam_meta()
    get_lcm_meta()
    get_ccm_meta()
    get_rcm_meta()
    get_lcdm_meta()
    get_ccdm_meta()
    get_rcdm_meta()
    get_lwb_meta()
    get_lb_meta()
    get_lcb_meta()
    get_ccb_meta()
    get_rcb_meta()
    get_rwb_meta()
    get_rb_meta()
    get_gk_meta()
    return 'Meta ratings calculated'

# function for player repeat checking
def exists(test_list, value):
    do_exist = False
    for element in test_list:
        if element == value:
            do_exist = True
    return do_exist

def get_squad_by_league(league):

    player_list = []
    squad_dict = {
        'LST': {},
        'RST': {},
        'LM': {},
        'LCM': {},
        'RCM': {},
        'RM': {},
        'LB': {},
        'LCB': {},
        'RCB': {},
        'RB': {},
        'GK': {}
    }

    lst_list = Player.query.filter_by(**{'league' : league}).order_by(Player.lst_meta_rating.desc()).limit(10)  
    rst_list = Player.query.filter_by(**{'league' : league}).order_by(Player.rst_meta_rating.desc()).limit(10)
    lm_list = Player.query.filter_by(**{'league' : league}).order_by(Player.lm_meta_rating.desc()).limit(10)
    lcm_list = Player.query.filter_by(**{'league' : league}).order_by(Player.ccdm_meta_rating.desc()).limit(10)
    rcm_list = Player.query.filter_by(**{'league' : league}).order_by(Player.rcm_meta_rating.desc()).limit(10)
    rm_list = Player.query.filter_by(**{'league' : league}).order_by(Player.rm_meta_rating.desc()).limit(10)
    lb_list = Player.query.filter_by(**{'league' : league}).order_by(Player.lb_meta_rating.desc()).limit(10)
    lcb_list = Player.query.filter_by(**{'league' : league}).order_by(Player.lcb_meta_rating.desc()).limit(10)
    rcb_list = Player.query.filter_by(**{'league' : league}).order_by(Player.rcb_meta_rating.desc()).limit(10)
    rb_list = Player.query.filter_by(**{'league' : league}).order_by(Player.rb_meta_rating.desc()).limit(10)
    gk_list = Player.query.filter_by(**{'league' : league}).order_by(Player.gk_meta_rating.desc()).limit(10)

    for player in lst_list:
        if not exists(player_list, player):
            player_list.append(player)
            squad_dict["LST"] = player
            break
    
    for player in rst_list:
        if not exists(player_list, player):
            player_list.append(player)
            squad_dict["RST"] = player
            break
    
    for player in lm_list:
        if not exists(player_list, player):
            player_list.append(player)
            squad_dict["LM"] = player
            break
    
    for player in lcm_list:
        if not exists(player_list, player):
            player_list.append(player)
            squad_dict["LCM"] = player
            break

    for player in rcm_list:
        if not exists(player_list, player):
            player_list.append(player)
            squad_dict["RCM"] = player
            break

    for player in rm_list:
        if not exists(player_list, player):
            player_list.append(player)
            squad_dict["RM"] = player
            break
    
    for player in lb_list:
        if not exists(player_list, player):
            player_list.append(player)
            squad_dict["LB"] = player
            break
    
    for player in lcb_list:
        if not exists(player_list, player):
            player_list.append(player)
            squad_dict["LCB"] = player
            break
    
    for player in rcb_list:
        if not exists(player_list, player):
            player_list.append(player)
            squad_dict["RCB"] = player
            break

    for player in rb_list:
        if not exists(player_list, player):
            player_list.append(player)
            squad_dict["RB"] = player
            break
    
    for player in gk_list:
        if not exists(player_list, player):
            player_list.append(player)
            squad_dict["GK"] = player
            break
    
    for key, value in squad_dict.items():
        #get_images_for_player(value)
        squad_dict[key] = value.serialize

    data = jsonify(squad_dict)

    data_list = [
        { 'position': 'LST', 'player_data': squad_dict['LST']},
        { 'position': 'RST', 'player_data': squad_dict['RST'] },
        { 'position': 'LM', 'player_data': squad_dict['LM'] },
        { 'position': 'LCM', 'player_data': squad_dict['LCM'] },
        { 'position': 'RCM', 'player_data': squad_dict['RCM'] },
        { 'position': 'RM', 'player_data': squad_dict['RM'] },
        { 'position': 'LB', 'player_data': squad_dict['LB'] },
        { 'position': 'LCB', 'player_data': squad_dict['LCB'] },
        { 'position': 'RCB', 'player_data': squad_dict['RCB']},
        { 'position': 'RB', 'player_data': squad_dict['RB'] },
        { 'position': 'GK', 'player_data': squad_dict['GK']}
    ]

    return jsonify(data_list)


def get_images_for_player(player):
        headers = {
            'accept': '*/*',
            'Content-Type': 'application/json',
            'X-AUTH-TOKEN': '{}'.format(apiKey)
        }
        try:
            response = requests.get('https://futdb.app/api/players/8/image', headers=headers).text
            #render_data = base64.b64encode(response).decode('ascii')
            #print(render_data)
            player_item = Player.query.get(player.id)
            player_item.face_image = base64.b64encode(response)
            db.session.commit()
        except:
            print("error during image requests")
            return None

        return None

## find way to concat lists LST CST RST and CF,   or filtering by two parameters,  or else do it the long way : one function for each position
def get_csts(league):
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.cst_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def get_cfs(league):
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.cf_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def get_lws(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.lw_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def get_rws(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.rw_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def get_ccams(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.ccam_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def get_ccms(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.ccm_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def get_ccdms(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.ccdm_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def get_lbs(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.lb_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def get_rbs(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.rb_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def get_ccbs(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.ccb_meta_rating.desc()).limit(10).all()
    #map(lambda player: print(player.serialize()), meta_rating_list)
    data = jsonify(data=[i.serialize for i in meta_rating_list])
    #return jsonify(meta_rating_list)
    return data

def get_gks(league):
    
    meta_rating_list = Player.query.filter_by(**{'league' : league}).order_by(Player.gk_meta_rating.desc()).limit(10).all()
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

def get_lw_meta():
    lw_meta = meta_weights.lw
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        lw_meta_rating = (player.sprint_speed * lw_meta["sprint_speed"] + player.finishing * lw_meta["finishing"]
            + player.dribbling * lw_meta["dribbling"] + player.acceleration * lw_meta["acceleration"]
            + player.positioning * lw_meta["positioning"] + player.shot_power * lw_meta["shot_power"]
            + player.agility * lw_meta["agility"] + player.vision * lw_meta["vision"]
            + player.crossing * lw_meta["crossing"] + player.short_passing * lw_meta["short_passing"]
            + player.balance * lw_meta["balance"] + player.composure * lw_meta["stamina"] + player.jumping * lw_meta["stamina"])
        
        if player.position == 'LW' or player.position == 'LM' or player.position == 'LF': lw_meta_rating += 4
        if player.foot == "Right": lw_meta_rating += 3
        lw_meta_rating += player.weak_foot * 1.5
        lw_meta_rating += player.skill_moves * 1.5

        player.lw_meta_rating = round(lw_meta_rating, 2)
        db.session.commit()
    return None

def get_lf_meta():
    lf_meta = meta_weights.lf
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        lf_meta_rating = (player.sprint_speed * lf_meta["sprint_speed"] + player.finishing * lf_meta["finishing"]
            + player.dribbling * lf_meta["dribbling"] + player.acceleration * lf_meta["acceleration"]
            + player.positioning * lf_meta["positioning"] + player.shot_power * lf_meta["shot_power"]
            + player.agility * lf_meta["agility"] + player.vision * lf_meta["vision"]
            + player.crossing * lf_meta["crossing"] + player.short_passing * lf_meta["short_passing"]
            + player.balance * lf_meta["balance"] + player.composure * lf_meta["stamina"] + player.jumping * lf_meta["stamina"])
        
        if player.position == 'LW' or player.position == 'LM' or player.position == 'LF': lf_meta_rating += 4
        if player.foot == "Right": lf_meta_rating += 3
        lf_meta_rating += player.weak_foot * 1.5
        lf_meta_rating += player.skill_moves * 1.5

        player.lf_meta_rating = round(lf_meta_rating, 2)
        db.session.commit()
    return None

def get_lm_meta():
    lm_meta = meta_weights.lm
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        lm_meta_rating = (player.sprint_speed * lm_meta["sprint_speed"] + player.finishing * lm_meta["finishing"]
            + player.dribbling * lm_meta["dribbling"] + player.acceleration * lm_meta["acceleration"]
            + player.positioning * lm_meta["positioning"] + player.shot_power * lm_meta["shot_power"]
            + player.agility * lm_meta["agility"] + player.vision * lm_meta["vision"]
            + player.crossing * lm_meta["crossing"] + player.short_passing * lm_meta["short_passing"]
            + player.balance * lm_meta["balance"] + player.composure * lm_meta["stamina"] + player.jumping * lm_meta["stamina"])
        
        if player.position == 'LW' or player.position == 'LM' or player.position == 'LF': lm_meta_rating += 4
        if player.foot == "Right": lm_meta_rating += 3
        lm_meta_rating += player.weak_foot * 1.5
        lm_meta_rating += player.skill_moves * 1.5

        player.lm_meta_rating = round(lm_meta_rating, 2)
        db.session.commit()
    return None

def get_lst_meta():
    lst_meta = meta_weights.lst
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        lst_meta_rating = (player.sprint_speed * lst_meta["sprint_speed"] + player.acceleration * lst_meta["acceleration"]
            + player.finishing * lst_meta["finishing"] + player.positioning * lst_meta["positioning"] + player.shot_power * lst_meta["shot_power"]
            + player.short_passing * lst_meta["short_passing"]
            + player.dribbling * lst_meta["dribbling"] + player.reactions * lst_meta["reactions"] + player.agility * lst_meta["agility"]
            + player.ball_control * lst_meta["ball_control"] + player.composure * lst_meta["composure"]
            + player.strength * lst_meta["strength"] + player.jumping * lst_meta["jumping"])
            
        if player.position == 'LF' or player.position == 'ST' or player.position == 'CF': lst_meta_rating += 4
        if player.foot == "Left": lst_meta_rating += 0.04
        lst_meta_rating += player.height * 0.01
        lst_meta_rating += player.weak_foot * 1.5
        lst_meta_rating += player.skill_moves * 1.5

        player.lst_meta_rating = round(lst_meta_rating, 2)
        db.session.commit()
    return None

def get_cst_meta():
    cst_meta = meta_weights.cst
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        cst_meta_rating = (player.sprint_speed * cst_meta["sprint_speed"] + player.acceleration * cst_meta["acceleration"]
            + player.finishing * cst_meta["finishing"] + player.positioning * cst_meta["positioning"] + player.shot_power * cst_meta["shot_power"]
            + player.short_passing * cst_meta["short_passing"]
            + player.dribbling * cst_meta["dribbling"] + player.reactions * cst_meta["reactions"] + player.agility * cst_meta["agility"]
            + player.ball_control * cst_meta["ball_control"] + player.composure * cst_meta["composure"]
            + player.strength * cst_meta["strength"] + player.jumping * cst_meta["jumping"])

        if player.position == 'ST' or player.position == 'CF': cst_meta_rating += 4
        cst_meta_rating += player.height * 0.01
        cst_meta_rating += player.weak_foot * 1.5
        cst_meta_rating += player.skill_moves * 1.5

        player.cst_meta_rating = round(cst_meta_rating, 2)
        db.session.commit()
    return None

def get_rst_meta():
    rst_meta = meta_weights.rst
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        rst_meta_rating = (player.sprint_speed * rst_meta["sprint_speed"] + player.acceleration * rst_meta["acceleration"]
            + player.finishing * rst_meta["finishing"] + player.positioning * rst_meta["positioning"] + player.shot_power * rst_meta["shot_power"]
            + player.short_passing * rst_meta["short_passing"]
            + player.dribbling * rst_meta["dribbling"] + player.reactions * rst_meta["reactions"] + player.agility * rst_meta["agility"]
            + player.ball_control * rst_meta["ball_control"] + player.composure * rst_meta["composure"]
            + player.strength * rst_meta["strength"] + player.jumping * rst_meta["jumping"])

        if player.position == 'RF' or player.position == 'ST' or player.position == 'CF': rst_meta_rating += 4    
        if player.foot == "Right": rst_meta_rating += 4
        rst_meta_rating += player.height * 0.01
        rst_meta_rating += player.weak_foot * 1.5
        rst_meta_rating += player.skill_moves * 1.5

        player.rst_meta_rating = round(rst_meta_rating, 2)
        db.session.commit()
    return None

def get_cf_meta():
    cf_meta = meta_weights.cf
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        cf_meta_rating = (player.sprint_speed * cf_meta["sprint_speed"] + player.acceleration * cf_meta["acceleration"]
            + player.finishing * cf_meta["finishing"] + player.positioning * cf_meta["positioning"] + player.shot_power * cf_meta["shot_power"]
            + player.short_passing * cf_meta["short_passing"]
            + player.dribbling * cf_meta["dribbling"] + player.reactions * cf_meta["reactions"] + player.agility * cf_meta["agility"]
            + player.ball_control * cf_meta["ball_control"] + player.composure * cf_meta["composure"]
            + player.strength * cf_meta["strength"] + player.jumping * cf_meta["jumping"])
         
        if player.position == 'ST' or player.position == 'CF': cf_meta_rating += 4   
        cf_meta_rating += player.height * 0.01
        cf_meta_rating += player.weak_foot * 1.5
        cf_meta_rating += player.skill_moves * 1.5

        player.cf_meta_rating = round(cf_meta_rating, 2)
        db.session.commit()
    return None

def nofn():
    return 'dummy'

def get_rw_meta():
    rw_meta = meta_weights.rw
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        rw_meta_rating = (player.sprint_speed * rw_meta["sprint_speed"] + player.finishing * rw_meta["finishing"]
            + player.dribbling * rw_meta["dribbling"] + player.acceleration * rw_meta["acceleration"]
            + player.positioning * rw_meta["positioning"] + player.shot_power * rw_meta["shot_power"]
            + player.agility * rw_meta["agility"] + player.vision * rw_meta["vision"]
            + player.crossing * rw_meta["crossing"] + player.short_passing * rw_meta["short_passing"]
            + player.balance * rw_meta["balance"] + player.composure * rw_meta["stamina"] + player.jumping * rw_meta["stamina"])
        
        if player.position == 'RW' or player.position == 'RM' or player.position == 'RF': rw_meta_rating += 4
        if player.foot == "Left": rw_meta_rating += 3
        rw_meta_rating += player.weak_foot * 1.5
        rw_meta_rating += player.skill_moves * 1.5

        player.rw_meta_rating = round(rw_meta_rating, 2)
        db.session.commit()
    return None

def get_rf_meta():
    rf_meta = meta_weights.rf
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        rf_meta_rating = (player.sprint_speed * rf_meta["sprint_speed"] + player.finishing * rf_meta["finishing"]
            + player.dribbling * rf_meta["dribbling"] + player.acceleration * rf_meta["acceleration"]
            + player.positioning * rf_meta["positioning"] + player.shot_power * rf_meta["shot_power"]
            + player.agility * rf_meta["agility"] + player.vision * rf_meta["vision"]
            + player.crossing * rf_meta["crossing"] + player.short_passing * rf_meta["short_passing"]
            + player.balance * rf_meta["balance"] + player.composure * rf_meta["stamina"] + player.jumping * rf_meta["stamina"])
        
        if player.position == 'RW' or player.position == 'RM' or player.position == 'RF': rf_meta_rating += 4
        if player.foot == "Left": rf_meta_rating += 0.04
        rf_meta_rating += player.weak_foot * 1.5
        rf_meta_rating += player.skill_moves * 1.5

        player.rf_meta_rating = round(rf_meta_rating, 2)
        db.session.commit()
    return None

def get_rm_meta():
    rm_meta = meta_weights.rm
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        rm_meta_rating = (player.sprint_speed * rm_meta["sprint_speed"] + player.finishing * rm_meta["finishing"]
            + player.dribbling * rm_meta["dribbling"] + player.acceleration * rm_meta["acceleration"]
            + player.positioning * rm_meta["positioning"] + player.shot_power * rm_meta["shot_power"]
            + player.agility * rm_meta["agility"] + player.vision * rm_meta["vision"]
            + player.crossing * rm_meta["crossing"] + player.short_passing * rm_meta["short_passing"]
            + player.balance * rm_meta["balance"] + player.composure * rm_meta["stamina"] + player.jumping * rm_meta["stamina"])
        
        if player.position == 'RW' or player.position == 'RM' or player.position == 'RF': rm_meta_rating += 4
        if player.foot == "Left": rm_meta_rating += 4
        rm_meta_rating += player.weak_foot * 1.5
        rm_meta_rating += player.skill_moves * 1.5

        player.rm_meta_rating = round(rm_meta_rating, 2)
        db.session.commit()
    return None

def get_lcam_meta():
    lcam_meta = meta_weights.lcam
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        lcam_meta_rating = (player.sprint_speed * lcam_meta["sprint_speed"] + player.finishing * lcam_meta["finishing"]
            + player.dribbling * lcam_meta["dribbling"] + player.acceleration * lcam_meta["acceleration"]
            + player.positioning * lcam_meta["positioning"] + player.shot_power * lcam_meta["shot_power"]
            + player.agility * lcam_meta["agility"] + player.vision * lcam_meta["vision"]
            + player.crossing * lcam_meta["crossing"] + player.short_passing * lcam_meta["short_passing"]
            + player.balance * lcam_meta["balance"] + player.composure * lcam_meta["stamina"] + player.jumping * lcam_meta["stamina"])
        

        if player.foot == "Right": lcam_meta_rating += 0.04
        lcam_meta_rating += player.weak_foot * 1.5
        lcam_meta_rating += player.skill_moves * 1.5
        player.lcam_meta_rating = round(lcam_meta_rating, 2)
        db.session.commit()
    return None

def get_ccam_meta():
    ccam_meta = meta_weights.ccam
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        ccam_meta_rating = (player.sprint_speed * ccam_meta["sprint_speed"] + player.finishing * ccam_meta["finishing"]
            + player.dribbling * ccam_meta["dribbling"] + player.acceleration * ccam_meta["acceleration"]
            + player.positioning * ccam_meta["positioning"] + player.shot_power * ccam_meta["shot_power"] + player.long_shots * ccam_meta["long_shots"]
            + player.agility * ccam_meta["agility"]
            + player.strength * ccam_meta["strength"] + player.short_passing * ccam_meta["short_passing"] + player.long_passing * ccam_meta["long_passing"]
            + player.balance * ccam_meta["balance"] + player.composure * ccam_meta["composure"] + player.vision * ccam_meta["vision"] 
            + player.stamina * ccam_meta["stamina"])

        ccam_meta_rating += player.weak_foot * 1.5
        ccam_meta_rating += player.skill_moves * 1.5

        player.ccam_meta_rating = round(ccam_meta_rating, 2)
        db.session.commit()
    return None

def get_rcam_meta():
    rcam_meta = meta_weights.rcam
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        rcam_meta_rating = (player.sprint_speed * rcam_meta["sprint_speed"] + player.finishing * rcam_meta["finishing"]
            + player.dribbling * rcam_meta["dribbling"] + player.acceleration * rcam_meta["acceleration"]
            + player.positioning * rcam_meta["positioning"] + player.shot_power * rcam_meta["shot_power"]
            + player.agility * rcam_meta["agility"] + player.vision * rcam_meta["vision"]
            + player.crossing * rcam_meta["crossing"] + player.short_passing * rcam_meta["short_passing"]
            + player.balance * rcam_meta["balance"] + player.composure * rcam_meta["stamina"] + player.jumping * rcam_meta["stamina"])
        

        if player.foot == "Left": rcam_meta_rating += 0.04
        rcam_meta_rating += player.weak_foot * 1.5
        rcam_meta_rating += player.skill_moves * 1.5
        player.rcam_meta_rating = round(rcam_meta_rating, 2)
        db.session.commit()
    return None


def get_lcm_meta():
    lcm_meta = meta_weights.lcm
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        lcm_meta_rating = (player.sprint_speed * lcm_meta["sprint_speed"] + player.acceleration * lcm_meta["acceleration"] 
            + player.finishing * lcm_meta["finishing"] + player.long_shots * lcm_meta["long_shots"] + player.reactions * lcm_meta["reactions"]
            + player.agility * lcm_meta["agility"] + player.balance * lcm_meta["balance"]
            + player.long_passing * lcm_meta["long_passing"] + player.short_passing * lcm_meta["short_passing"] + player.vision * lcm_meta["vision"]
            + player.strength * lcm_meta["strength"] + player.stamina * lcm_meta["stamina"] + player.jumping * lcm_meta["jumping"])

        if player.position == 'CM': lcm_meta_rating += 4
        if player.foot == "Left": lcm_meta_rating += 0.02
        lcm_meta_rating += player.weak_foot * 1
        lcm_meta_rating += player.skill_moves * 0.75
        if player.attack_work_rate == "high": lcm_meta_rating += 3
        elif player.attack_work_rate == "med": lcm_meta_rating += 1
        if player.defense_work_rate == "high": lcm_meta_rating += 3
        elif player.defense_work_rate == "med": lcm_meta_rating += 1

        player.lcm_meta_rating = round(lcm_meta_rating, 2)
        db.session.commit()
       
    return None

def get_ccm_meta():
    ccm_meta = meta_weights.ccm
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        ccm_meta_rating = (player.sprint_speed * ccm_meta["sprint_speed"] + player.acceleration * ccm_meta["acceleration"] 
            + player.finishing * ccm_meta["finishing"] + player.long_shots * ccm_meta["long_shots"] + player.reactions * ccm_meta["reactions"]
            + player.agility * ccm_meta["agility"] + player.balance * ccm_meta["balance"]
            + player.long_passing * ccm_meta["long_passing"] + player.short_passing * ccm_meta["short_passing"] + player.vision * ccm_meta["vision"]
            + player.strength * ccm_meta["strength"] + player.stamina * ccm_meta["stamina"] + player.jumping * ccm_meta["jumping"])

        if player.position == 'CM': ccm_meta_rating += 4
        ccm_meta_rating += player.weak_foot * 1
        ccm_meta_rating += player.skill_moves * 0.75
        ccm_meta_rating += player.height * 0.01
        if player.attack_work_rate == "high": ccm_meta_rating += 3
        elif player.attack_work_rate == "med": ccm_meta_rating += 1
        if player.defense_work_rate == "high": ccm_meta_rating += 3
        elif player.defense_work_rate == "med": ccm_meta_rating += 1

        player.ccm_meta_rating = round(ccm_meta_rating, 2)
        db.session.commit()
       
    return None

def get_rcm_meta():
    rcm_meta = meta_weights.rcm
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        rcm_meta_rating = (player.sprint_speed * rcm_meta["sprint_speed"] + player.acceleration * rcm_meta["acceleration"] 
            + player.finishing * rcm_meta["finishing"] + player.long_shots * rcm_meta["long_shots"] + player.reactions * rcm_meta["reactions"]
            + player.agility * rcm_meta["agility"] + player.balance * rcm_meta["balance"]
            + player.long_passing * rcm_meta["long_passing"] + player.short_passing * rcm_meta["short_passing"] + player.vision * rcm_meta["vision"]
            + player.strength * rcm_meta["strength"] + player.stamina * rcm_meta["stamina"] + player.jumping * rcm_meta["jumping"])

        if player.position == 'CM': rcm_meta_rating += 4
        if player.foot == "Right": rcm_meta_rating += 0.02
        rcm_meta_rating += player.weak_foot * 1
        rcm_meta_rating += player.skill_moves * 0.75
        if player.attack_work_rate == "high": rcm_meta_rating += 3
        elif player.attack_work_rate == "med": rcm_meta_rating += 1
        if player.defense_work_rate == "high": rcm_meta_rating += 3
        elif player.defense_work_rate == "med": rcm_meta_rating += 1

        player.rcm_meta_rating = round(rcm_meta_rating, 2)
        db.session.commit()
       
    return None

def get_lcdm_meta():
    lcdm_meta = meta_weights.lcdm
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        lcdm_meta_rating = (player.sprint_speed * lcdm_meta["sprint_speed"]
            + player.long_passing * lcdm_meta["long_passing"] + player.acceleration * lcdm_meta["acceleration"]
            + player.strength * lcdm_meta["strength"] + player.short_passing * lcdm_meta["short_passing"]
            + player.balance * lcdm_meta["balance"] + player.dribbling * lcdm_meta["dribbling"] + player.jumping * lcdm_meta["jumping"]
            + player.interceptions * lcdm_meta["interceptions"] + player.standing_tackle * lcdm_meta["standing_tackle"] + 
            + player.aggression * lcdm_meta["aggression"])
        
        if player.position == 'CDM': lcdm_meta_rating += 4
        if player.foot == "Left": lcdm_meta_rating += 0.02
        lcdm_meta_rating += player.weak_foot * 1
        lcdm_meta_rating += player.skill_moves * 0.75
        lcdm_meta_rating += player.height * 0.01
        if player.attack_work_rate == "high": lcdm_meta_rating += 3
        elif player.attack_work_rate == "med": lcdm_meta_rating += 1
        if player.defense_work_rate == "high": lcdm_meta_rating += 3
        elif player.defense_work_rate == "med": lcdm_meta_rating += 1

        player.lcdm_meta_rating = round(lcdm_meta_rating, 2)
        db.session.commit()
    return None

def get_ccdm_meta():
    ccdm_meta = meta_weights.ccdm
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        ccdm_meta_rating = (player.sprint_speed * ccdm_meta["sprint_speed"]
            + player.long_passing * ccdm_meta["long_passing"] + player.acceleration * ccdm_meta["acceleration"]
            + player.strength * ccdm_meta["strength"] + player.short_passing * ccdm_meta["short_passing"]
            + player.balance * ccdm_meta["balance"] + player.dribbling * ccdm_meta["dribbling"] + player.jumping * ccdm_meta["jumping"]
            + player.interceptions * ccdm_meta["interceptions"] + player.standing_tackle * ccdm_meta["standing_tackle"] + 
            + player.aggression * ccdm_meta["aggression"])
        
        if player.position == 'CDM': ccdm_meta_rating += 4
        ccdm_meta_rating += player.weak_foot * 1
        ccdm_meta_rating += player.skill_moves * 0.75
        ccdm_meta_rating += player.height * 0.01
        if player.attack_work_rate == "high": ccdm_meta_rating += 3
        elif player.attack_work_rate == "med": ccdm_meta_rating += 1
        if player.defense_work_rate == "high": ccdm_meta_rating += 3
        elif player.defense_work_rate == "med": ccdm_meta_rating += 1

        player.ccdm_meta_rating = round(ccdm_meta_rating, 2)
        db.session.commit()
    return None

def get_rcdm_meta():
    rcdm_meta = meta_weights.rcdm
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        rcdm_meta_rating = (player.sprint_speed * rcdm_meta["sprint_speed"]
            + player.long_passing * rcdm_meta["long_passing"] + player.acceleration * rcdm_meta["acceleration"]
            + player.strength * rcdm_meta["strength"] + player.short_passing * rcdm_meta["short_passing"]
            + player.balance * rcdm_meta["balance"] + player.dribbling * rcdm_meta["dribbling"] + player.jumping * rcdm_meta["jumping"]
            + player.interceptions * rcdm_meta["interceptions"] + player.standing_tackle * rcdm_meta["standing_tackle"] + 
            + player.aggression * rcdm_meta["aggression"])
        
        if player.position == 'CDM': rcdm_meta_rating += 4
        if player.foot == "Right": rcdm_meta_rating += 0.02
        rcdm_meta_rating += player.weak_foot * 1
        rcdm_meta_rating += player.skill_moves * 0.75
        rcdm_meta_rating += player.height * 0.01
        if player.attack_work_rate == "high": rcdm_meta_rating += 3
        elif player.attack_work_rate == "med": rcdm_meta_rating += 1
        if player.defense_work_rate == "high": rcdm_meta_rating += 3
        elif player.defense_work_rate == "med": rcdm_meta_rating += 1

        player.rcdm_meta_rating = round(rcdm_meta_rating, 2)
        db.session.commit()
    return None

def get_lwb_meta():
    lwb_meta = meta_weights.lwb
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        lwb_meta_rating = (player.sprint_speed * lwb_meta["sprint_speed"] + player.acceleration * lwb_meta["acceleration"]
            + player.interceptions * lwb_meta["interceptions"] + player.standing_tackle * lwb_meta["standing_tackle"]
            + player.dribbling * lwb_meta["dribbling"] + player.agility * lwb_meta["agility"] + player.balance * lwb_meta["balance"]
            + player.short_passing * lwb_meta["short_passing"] + player.long_passing * lwb_meta["long_passing"]  + player.vision * lwb_meta["vision"]
            + player.strength * lwb_meta["strength"] + player.stamina * lwb_meta["stamina"])

        if player.position == 'LB' or player.position == 'LWB': lwb_meta_rating += 4
        if player.foot == "Left": lwb_meta_rating += 0.04
        lwb_meta_rating += player.weak_foot * 1
        lwb_meta_rating += player.skill_moves * 1
        lwb_meta_rating += player.height * 0.01
        if player.attack_work_rate == "high": lwb_meta_rating += 3
        elif player.attack_work_rate == "med": lwb_meta_rating += 1
        if player.defense_work_rate == "high": lwb_meta_rating += 3
        elif player.defense_work_rate == "med": lwb_meta_rating += 1

        player.lwb_meta_rating = round(lwb_meta_rating, 2)
        db.session.commit()
    return None

def get_lb_meta():
    lb_meta = meta_weights.lb
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        lb_meta_rating = (player.sprint_speed * lb_meta["sprint_speed"] + player.acceleration * lb_meta["acceleration"]
            + player.interceptions * lb_meta["interceptions"] + player.standing_tackle * lb_meta["standing_tackle"]
            + player.dribbling * lb_meta["dribbling"] + player.agility * lb_meta["agility"] + player.balance * lb_meta["balance"]
            + player.short_passing * lb_meta["short_passing"] + player.long_passing * lb_meta["long_passing"]  + player.vision * lb_meta["vision"]
            + player.strength * lb_meta["strength"] + player.stamina * lb_meta["stamina"])

        if player.position == 'LB' or player.position == 'LWB': lb_meta_rating += 4   
        if player.foot == "Left": lb_meta_rating += 0.04
        lb_meta_rating += player.weak_foot * 1
        lb_meta_rating += player.skill_moves * 1
        lb_meta_rating += player.height * 0.01
        if player.attack_work_rate == "low": lb_meta_rating += 3
        elif player.attack_work_rate == "med": lb_meta_rating += 1
        if player.defense_work_rate == "high": lb_meta_rating += 3
        elif player.defense_work_rate == "med": lb_meta_rating += 1

        player.lb_meta_rating = round(lb_meta_rating, 2)
        db.session.commit()
    return None

def get_lcb_meta():
    lcb_meta = meta_weights.lcb
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        lcb_meta_rating = (player.sprint_speed * lcb_meta["sprint_speed"] + player.acceleration * lcb_meta["acceleration"]
            + player.agility * lcb_meta["agility"] + player.reactions * lcb_meta["reactions"]
             + player.short_passing * lcb_meta["short_passing"] + player.long_passing * lcb_meta["long_passing"]
            + player.composure * lcb_meta["composure"] + player.jumping * lcb_meta["jumping"] + player.aggression * lcb_meta["aggression"] + player.strength * lcb_meta["strength"]
            + player.interceptions * lcb_meta["interceptions"] + player.sliding_tackle * lcb_meta["sliding_tackle"] + player.standing_tackle * lcb_meta["standing_tackle"]) 

        if player.position == 'CB': lcb_meta_rating += 4
        if player.position == 'LB' or player.position == 'RB' or player.position == 'CDM': lcb_meta_rating += 2
        lcb_meta_rating += player.height * 0.01
        if player.foot == "Left": lcb_meta_rating += 0.04
        if player.attack_work_rate == "low": lcb_meta_rating += 3
        elif player.attack_work_rate == "med": lcb_meta_rating += 1
        if player.defense_work_rate == "high": lcb_meta_rating += 3
        elif player.defense_work_rate == "med": lcb_meta_rating += 1

        player.lcb_meta_rating = round(lcb_meta_rating, 2)
        db.session.commit()
    return None

def get_ccb_meta():
    ccb_meta = meta_weights.ccb
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        ccb_meta_rating = (player.sprint_speed * ccb_meta["sprint_speed"] + player.acceleration * ccb_meta["acceleration"]
            + player.agility * ccb_meta["agility"] + player.reactions * ccb_meta["reactions"]
             + player.short_passing * ccb_meta["short_passing"] + player.long_passing * ccb_meta["long_passing"]
            + player.composure * ccb_meta["composure"] + player.jumping * ccb_meta["jumping"] + player.aggression * ccb_meta["aggression"] + player.strength * ccb_meta["strength"]
            + player.interceptions * ccb_meta["interceptions"] + player.sliding_tackle * ccb_meta["sliding_tackle"] + player.standing_tackle * ccb_meta["standing_tackle"]) 

        if player.position == 'CB': ccb_meta_rating += 4
        if player.position == 'LB' or player.position == 'RB' or player.position == 'CDM': ccb_meta_rating += 2
        ccb_meta_rating += player.height * 0.01
        if player.attack_work_rate == "low": ccb_meta_rating += 3
        elif player.attack_work_rate == "med": ccb_meta_rating += 1
        if player.defense_work_rate == "high": ccb_meta_rating += 3
        elif player.defense_work_rate == "med": ccb_meta_rating += 1

        player.ccb_meta_rating = round(ccb_meta_rating, 2)
        db.session.commit()
    return None

def get_rcb_meta():
    rcb_meta = meta_weights.rcb
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        rcb_meta_rating = (player.sprint_speed * rcb_meta["sprint_speed"] + player.acceleration * rcb_meta["acceleration"]
            + player.agility * rcb_meta["agility"] + player.reactions * rcb_meta["reactions"]
             + player.short_passing * rcb_meta["short_passing"] + player.long_passing * rcb_meta["long_passing"]
            + player.composure * rcb_meta["composure"] + player.jumping * rcb_meta["jumping"] + player.aggression * rcb_meta["aggression"] + player.strength * rcb_meta["strength"]
            + player.interceptions * rcb_meta["interceptions"] + player.sliding_tackle * rcb_meta["sliding_tackle"] + player.standing_tackle * rcb_meta["standing_tackle"]) 

        if player.position == 'CB': rcb_meta_rating += 4
        if player.position == 'LB' or player.position == 'RB' or player.position == 'CDM': rcb_meta_rating += 2
        rcb_meta_rating += player.height * 0.01
        if player.foot == "Right": rcb_meta_rating += 0.04
        if player.attack_work_rate == "low": rcb_meta_rating += 3
        elif player.attack_work_rate == "med": rcb_meta_rating += 1
        if player.defense_work_rate == "high": rcb_meta_rating += 3
        elif player.defense_work_rate == "med": rcb_meta_rating += 1

        player.rcb_meta_rating = round(rcb_meta_rating, 2)
        db.session.commit()
    return None

def get_rwb_meta():
    rwb_meta = meta_weights.rwb
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        rwb_meta_rating = (player.sprint_speed * rwb_meta["sprint_speed"] + player.acceleration * rwb_meta["acceleration"]
            + player.interceptions * rwb_meta["interceptions"] + player.standing_tackle * rwb_meta["standing_tackle"]
            + player.dribbling * rwb_meta["dribbling"] + player.agility * rwb_meta["agility"] + player.balance * rwb_meta["balance"]
            + player.short_passing * rwb_meta["short_passing"] + player.long_passing * rwb_meta["long_passing"]  + player.vision * rwb_meta["vision"]
            + player.strength * rwb_meta["strength"] + player.stamina * rwb_meta["stamina"])

        if player.position == 'RB' or player.position == 'RWB': rwb_meta_rating += 4
        if player.foot == "Right": rwb_meta_rating += 0.04
        rwb_meta_rating += player.weak_foot * 1
        rwb_meta_rating += player.skill_moves * 1
        rwb_meta_rating += player.height * 0.01
        if player.attack_work_rate == "high": rwb_meta_rating += 3
        elif player.attack_work_rate == "med": rwb_meta_rating += 1
        if player.defense_work_rate == "high": rwb_meta_rating += 3
        elif player.defense_work_rate == "med": rwb_meta_rating += 1

        player.rwb_meta_rating = round(rwb_meta_rating, 2)
        db.session.commit()
    return None

def get_rb_meta():
    rb_meta = meta_weights.rb
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        rb_meta_rating = (player.sprint_speed * rb_meta["sprint_speed"] + player.acceleration * rb_meta["acceleration"]
            + player.interceptions * rb_meta["interceptions"] + player.standing_tackle * rb_meta["standing_tackle"]
            + player.dribbling * rb_meta["dribbling"] + player.agility * rb_meta["agility"] + player.balance * rb_meta["balance"]
            + player.short_passing * rb_meta["short_passing"] + player.long_passing * rb_meta["long_passing"]  + player.vision * rb_meta["vision"]
            + player.strength * rb_meta["strength"] + player.stamina * rb_meta["stamina"])

        if player.position == 'RB' or player.position == 'RWB': rb_meta_rating += 4   
        if player.foot == "Right": rb_meta_rating += 0.04
        rb_meta_rating += player.weak_foot * 1
        rb_meta_rating += player.skill_moves * 1
        rb_meta_rating += player.height * 0.01
        if player.attack_work_rate == "low": rb_meta_rating += 3
        elif player.attack_work_rate == "med": rb_meta_rating += 1
        if player.defense_work_rate == "high": rb_meta_rating += 3
        elif player.defense_work_rate == "med": rb_meta_rating += 1

        player.rb_meta_rating = round(rb_meta_rating, 2)
        db.session.commit()
    return None

def get_gk_meta():
    gk_meta = meta_weights.gk
    for i in range(1, db.session.query(Player).count(), 1):
        player = Player.query.get(i)
        
        gk_meta_rating = (player.sprint_speed * gk_meta["sprint_speed"] + player.acceleration * gk_meta["acceleration"]
            + player.diving * gk_meta["diving"] + player.handling * gk_meta["handling"]
             + player.short_passing * gk_meta["short_passing"] + player.long_passing * gk_meta["long_passing"]
            + player.kicking * gk_meta["kicking"] + player.gk_positioning * gk_meta["gk_positioning"] + player.reflexes * gk_meta["reflexes"]) 

        gk_meta_rating += player.height * 0.06

        player.gk_meta_rating = round(gk_meta_rating, 2)
        db.session.commit()
    return None

if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()
    print("Done!")
