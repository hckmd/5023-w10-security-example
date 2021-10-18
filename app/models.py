from app import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    owner = db.Column(db.Text)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'))
    animal = db.relationship('Animal')

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

