from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from views import *


app = Flask(__name__, static_folder='static')
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///futstarter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
app.config["JWT_SECRET_KEY"] = "serverkey"
jwt = JWTManager(app)

CORS(app)

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

# if __name__ == "__main__":  # if running in localhost
#     from views import *
#     app.run(host='0.0.0.0')