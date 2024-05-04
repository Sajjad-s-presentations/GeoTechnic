from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import mysql.connector


db = SQLAlchemy()

def getdb():
    if 'db' not in g or not g.db.is_connected():
        g.db = mysql.connector.connect(
            host=current_app.config['localhost'],
            user=current_app.config['root'],
            password=current_app.config[''],
            database=current_app.config['test'],
            ssl_verify_identity=True,
            ssl_ca='SSL/certs/ca-cert.pem'
        )
    return g.db

@app.route('/')
def home():
    connection = db.getdb()
    # Use the connection to interact with the database, e.g., execute queries

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'

    db.init_app(app)

    migrate = Migrate(app, db)


    return app
