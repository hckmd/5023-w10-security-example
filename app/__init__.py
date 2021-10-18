from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up configuration settings for connection to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# The secret key here is used for demonstration purposes - DO NOT USE IN PRODUCTION
app.config['SECRET_KEY'] = 'this-is-a-secret' 

# Registers for the blueprints for animal, pet and authentication
from app.animal import bp as animal_bp
app.register_blueprint(animal_bp, url_prefix='/animal')

from app.pet import bp as pet_bp
app.register_blueprint(pet_bp, url_prefix='/pet')

from app import routes
from app.models import Animal, Pet

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

    # Create pet owned by Jill
    desi = Pet(name='Desi', animal=dog, owner='jill')
    db.session.add(desi)

    # Create pets owned by Phil
    ebony = Pet(name='Ebony', animal=cat, owner='phil')
    db.session.add(ebony)
    ivory = Pet(name='Ivory', animal=cat, owner='phil')
    db.session.add(ivory)

    # Save the changes made to the records database
    db.session.commit()
