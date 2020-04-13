from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=False)
    last_name = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=False)
    currency = db.Column(db.String(8))
    total = db.Column(db.Float)
    day_chg = db.Column(db.Float)
    market_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.String(32), index=True)
    quantity = db.Column(db.Integer)
    latest_price = db.Column(db.Float)
    value = db.Column(db.Float)
    change = db.Column(db.Float)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'))


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(140))
    last_price = db.Column(db.Float)
    change = db.Column(db.Float)
    currency = db.Column(db.String(8))
    day_chg = db.Column(db.Float)
    market_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'))

