# futstarter-backend documentation
### FIFA FUT companion webapp for model-based meta-stat player sorting and team building. This initial version only includes the 442 formation for five different leagues. The player database is created by fetching the FUTDB API REST and the player sorting is based on an original meta rating calculation algorithm. 

# Table of contents
1. [Routes & Methods](#routes-&-methods)
    1. [Admin methods](#admin-methods)
        1. [Database methods](#database-methods)
    2. [User methods](#user-methods)
        1. [GET methods](#get-methods)
        2. [POST methods](#post-methods)
2. [Player data](#player-data)
    1. [Player JSON response attributes](#player-json-response-attributes)
    2. [Player positions](#player-positions)
3. [Squad data](#squad-data)
    1. [Squad JSON response](#squad-json-response)
    2. [Squad formations](#squad-formations1)

# 1. Routes & Methods
## 1.1 Admin methods
### 1.1.1 Database methods

#### To setup or update the player database the admin accesses:
    /update

#### This route runs two methods:
 
    update_player_db()

#### which updates the player database and populates the player table, excepting the meta-ratings that will be initialized with value 1,  and

    calculate_meta()

#### which calculates meta ratings and updates the position-relative meta ratings for each player of the Player table 

------
## 1.2 User methods

### 1.2.1 GET methods
#### -Players meta-rating rankings json data:
    GET /players/leagues/<int:league>/<str:position>   
    GET /players/nations/<int:nation>/<str:position>

With this data we can render player ranking lists in the Players view

#### -Calculated squads:
    GET /squads/leagues/<int:league>
    GET /squads/nations/<int:nation>

And also render the squads previosuly generated with the meta calculation model
### 1.2.2 POST methods
#### -Registering new user:
    POST /register 
    body = {
        "username": <str>,
        "email": <str>,
        "password": <str>
    }
    // OK response
    response = {
        "status": 200,
        "data": {
            "user": {
                "username": <str>,
                "email": <str>
            },
            "token": <str>
        }
    }
    // BAD response
    response = {
        "status": 400,
        "msg": <str>
    }

#### -Loging in:
    UPDATE /login
    body = {
        "email": <str>,
        "password": <str>
    }

# 2. Player data
## 2.1 Player JSON response attributes
    [
        {
            "id": <int>,
            "resource_id": <int>,
            "rarity": <int>,
            "common_name": <str>,
            "name": <str>,
            "first_name": <str>,
            "last_name": <str>,
            "rating": <int>,
            "st_meta_rating": <int>,
            "wing_meta_rating": <int>,
            "cam_meta_rating": <int>,
            "cm_meta_rating": <int>,
            "cdm_meta_rating": <int>,
            "fb_meta_rating": <int,>
            "cb_meta_rating": <int>,
            "nation": <int>,
            "league" : <int>, 
            "club" : <int>,
            "position" : <str>,
            "height" : <int>,
            "weight" : <int>,
            "attack_work_rate" : <int>,
            "defense_work_rate" : <int>,
            "foot" : <str>,
            "weak_foot" : <int>,
            "skill_moves" : <int>,
            "shooting" : <int>,
            "positioning" : <int>,
            "finishing" : <int>,
            "shot_power" : <int>,
            "long_shots" : <int>,
            "volleys" : <int>,
            "penalties" : <int>,
            "defending" : <int>,
            "heading_accuracy" : <int>,
            "interceptions" : <int>,
            "sliding_tackle" : <int>,
            "standing_tackle" : <int>,
            "dribbling_face" : <int>,
            "agility" : <int>,
            "balance" : <int>,
            "ball_control" : <int>,
            "composure" : <int>,
            "dribbling" : <int>,
            "reactions" : <int>,
            "pace" : <int>,
            "acceleration" : <int>,
            "sprint_speed" : <int>,
            "passing" : <int>,
            "crossing" : <int>,
            "curve" : <int>,
            "free_kick_accuracy" : <int>,
            "long_passing" : <int>,
            "short_passing" : <int>,
            "vision" : <int>,
            "physicality" : <int>,
            "aggression" : <int>,
            "stamina" : <int>,
            "jumping" : <int>,
            "strength" : <int>
        },
        {...}
    ]

## 2.2 Player positions:
* LW/LM/LF
* LST/CST/RST/CF
* RW/RM/RF
* LCAM/CCAM/RCAM
* LCM/CCM/RCM
* LCDM/CCDM/RCDM
* LWB/LB
* LCB/CCB/RCB
* RWB/RB
* GK

## 2.3 Leagues:
* 13: Premier League
* 16: Ligue 1
* 19: Bundesliga
* 31: Serie A
* 53: LaLiga

# 3. Squad data

## 3.1 Squad JSON response

### For the 442 formation
    data = {
        'lst': {},
        'rst': {},
        'lm': {},
        'lcm': {},
        'rcm': {},
        'rm': {},
        'lb': {},
        'lcb': {},
        'rcb': {},
        'rb': {},
        'gk': {}
    }
## 3.2 Squad formations:

### For now only the 442 will be implemented, but in the future the model could include:

* 352: {GK, LCB, CCB, RCB, LM, LCDM, CAM, RCDM, RM, LST, RST}
* 41212: {GK, LB, LCB, RCB, RB, CDM, LM, CAM, RM, LST, RST}
* 41212(2): {GK, LB, LCB, RCB, RB, CDM, LCM, CAM, RCM, LST, RST}
* 4231: {GK, LB, LCB, RCB, RB, LCDM, RCDM, LCAM, CCAM, RCAM, ST}
* 4321: {GK, LB, LCB, RCB, RB, LCM, CCM, RCM, LF, ST, RF }
* 433: {GK, LB, LCB, RCB, RB, LCM, CCM, RCM, LW, ST, RW}
* 433(4): {GK, LB, LCB, RCB, RB, LCM, CAM, RCM, LW, ST, RW}
* 442: {GK, LB, LCB, RCB, RB, LM, LCM, RCM, RM, LST, RST}
* 532: {GK, LWB, LCB, CCB, RCB, RWB, LCM, CCM, RCM, LST, RST}



# Future updates:

Further improvements to the generated squad and the generator itself could be made. Ranging from the creation of a futbin-based approach of a squad builder, to the implementation of a user controlled, meta-weight modelling tool for squad generation. For example, imagine starting from a futbin-based user-built squad, and on top of it, tweaking the meta-weights to alter the team as desired.
Also, the database could be extendend to cover the entire FUT player database, every squad formation and any nation.






