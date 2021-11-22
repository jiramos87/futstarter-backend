from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///futstarter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#CORS(app)
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)



if __name__ == "__main__":
    from views import *
    app.run(host='0.0.0.0')