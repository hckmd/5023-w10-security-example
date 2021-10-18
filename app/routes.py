from flask import render_template
from flask_login import login_required

from app import app
from app.models import Pet

@app.route('/')
@login_required
def index():
    pets = Pet.query.all()
    return render_template('index.html', title = 'Home', pets = pets)
