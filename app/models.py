from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, primary_key=False)
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, primary_key=False)
    desciption = db.Column(db.Text, primary_key=False)
    price = db.Column(db.Text, primary_key=False)
        
