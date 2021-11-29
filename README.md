# futstarter-backend documentation
FIFA FUT companion webapp for model-based meta-stat player sorting and team building

## Admin methods
#### To update player database and populate the Player table stats, excepting the meta-ratings that will be initialized with value 1:
    /updateplayerdb

#### To calculate meta ratings and update the position-relative meta ratings in each element of the Player table  :
    /calculatemeta 

#### To generate squads based on the best players for each position by meta-sorting player lists:
    /generatesquads
## User methods

### GET methods
#### -Players meta-rating rankings json data:
    GET /players/leagues/<int:league>/<int:position>   
    GET /players/nations/<int:nation>/<int:position>

With this data we can render player ranking lists in the Players view

#### -Calculated squads:
    GET /squads/leagues/<int:league>/<int:position>
    GET /squads/nations/<int:nation>/<int:position>

And also render the squads previosuly generated with the meta calculation model
### POST methods
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

### DELETE methods
#### -Deleting user
    DELETE /users
    body = {

    }



## Future updates:

Further improvements to the generated squad and the generator itself could be made. Ranging from the creation of a futbin-based approach of a squad builder, to the implementation of a user controlled, meta-weight modelling tool for squad generation. For example, imagine starting from a futbin-based user-built squad, and on top of it, tweaking the meta-weights to alter the team as desired.





