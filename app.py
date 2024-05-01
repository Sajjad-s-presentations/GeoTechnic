from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

class Tariff_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_no = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String(1000))

with app.app_context():
    db.create_all()