from flask import render_template

from app import app
from app.models import Pet

@app.route('/')
def index():
    pets = Pet.query.all()
    return render_template('index.html', title = 'Home', pets = pets)
