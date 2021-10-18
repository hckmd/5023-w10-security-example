from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)
    pets = db.relationship('Pet', backref='owner')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'))
    animal = db.relationship('Animal')

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

