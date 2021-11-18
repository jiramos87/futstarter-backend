from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///futstarter.db'
db = SQLAlchemy(app)

if __name__ == "__main__":
    from views import *
    app.run(host='0.0.0.0')