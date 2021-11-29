# futstarter-backend documentation
FIFA FUT companion webapp for model-based meta-stat player sorting and team building

# Table of contents
1. [Routes & Methods](#routes-&-methods)
    1. [Admin methods](#admin-methods)
        1. [Database methods](#database-methods)
    2. [User methods](#user-methods)
        1. [GET methods](#get-methods)
        2. [POST methods](#post-methods)
        3. [DELETE methods](#delete-methods)
2. [Player data](#player-data)
    1. [Player JSON response attributes](#player-json-response-attributes)
    2. [Player positions](#player-positions)
3. [Squad data](#squad-data)
    1. [Squad JSON response](#squad-json-response)
    2. [Squad formations](#squad-formations1)

# 1. Routes & Methods
## 1.1 Admin methods
### 1.1.1 Database methods
#### To update player database and populate the Player table stats, excepting the meta-ratings that will be initialized with value 1:
    /updateplayerdb

#### To calculate meta ratings and update the position-relative meta ratings in each element of the Player table  :
    /calculatemeta 

#### To generate squads based on the best players for each position by meta-sorting player lists:
    /generatesquads

------
## 1.2 User methods

### 1.2.1 GET methods
#### -Players meta-rating rankings json data:
    GET /players/leagues/<int:league>/<int:position>   
    GET /players/nations/<int:nation>/<int:position>

With this data we can render player ranking lists in the Players view

#### -Calculated squads:
    GET /squads/leagues/<int:league>/<int:position>
    GET /squads/nations/<int:nation>/<int:position>

And also render the squads previosuly generated with the meta calculation model
### 1.2.2 POST methods
#### -Registering new user:
    POST /register 
    body = {

    }

#### -Loging in:
    UPDATE /login
    body = {

    }

#### -Loging out:
    UPDATE /login
    body = {

    }

#### -Changing password:
    UPDATE /user
    body = {

    }

#### -Saving squad
    POST /user/squads

### 1.2.3 DELETE methods
#### -Deleting user
    DELETE /users
    body = {

    }

# 2. Player data
## 2.1 Player JSON response attributes

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
        }

## 2.2 Player positions:
* LW/LM/LF
* ST/LST/RST/CF
* RW/RM/LF
* CAM/LCAM/CCAM/RCAM
* CM/LCM/CCM/RCM
* CDM/LCDM/RCDM
* LB/LWB
* CB/LCB/RCB
* RB/RWB
* GK

# 3. Squad data

## 3.1 Squad JSON response

    [
        "formation": "433",
        "LW" : { Player JSON... },
        "ST" : { Player JSON...},
        "RW": { Player JSON...},
        ...
    ]
## 3.2 Squad formations:

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





