from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///db.sqlite3'
app.config['SQLALCHEMY_TACK_MODIFICATIONS'] = False