from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)
    pets = db.relationship('Pet', backref='owner')

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'))
    animal = db.relationship('Animal')

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

