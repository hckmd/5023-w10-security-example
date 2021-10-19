import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

app = Flask(__name__)

# Set up configuration settings for connection to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# The secret key here is used for demonstration purposes - DO NOT USE IN PRODUCTION
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Registers for the blueprints for animal, pet and authentication
from app.animal import bp as animal_bp
app.register_blueprint(animal_bp, url_prefix='/animal')

from app.pet import bp as pet_bp
app.register_blueprint(pet_bp, url_prefix='/pet')

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

from app import routes
from app.models import Animal, Pet, User

@app.cli.command('init-db')
def init_db():

    # Recreate the database for the app
    db.drop_all()
    db.create_all()

    # Create animals in the system
    cat = Animal(name='Cat')
    dog = Animal(name='Dog')

    frog = Animal(name='Frog')
    db.session.add(frog)

    # Create Jill user with a pet Dog
    jill = User(username='jill', is_admin=False)
    jill.password = os.environ.get('JILL_PASSWORD')
    desi = Pet(name='Desi', animal=dog)
    jill.pets.append(desi)
    db.session.add(jill)

    # Create Phil user (admin) with two pets
    phil = User(username='phil', is_admin=True)
    phil.password = os.environ.get('PHIL_PASSWORD')
    ebony = Pet(name='Ebony', animal=cat)
    ivory = Pet(name='Ivory', animal=cat)
    phil.pets.append(ebony)
    phil.pets.append(ivory)
    db.session.add(phil)

    # Save the changes made to the records database
    db.session.commit()


