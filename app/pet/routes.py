from flask import render_template, redirect, url_for

from app import db
from app.pet import bp
from app.models import Animal, Pet
from .forms import AddPetForm, EditPetForm

@bp.route('/')
def my_pet_list():
    ''' A route for a list of all pets in the register . '''
    pets = Pet.query.all()
    return render_template('pet_list.html', title = 'Pets', pets = pets)

@bp.route('/<int:id>')
def pet_details(id):
    ''' A route that shows the details for a specific pet in the register. '''
    pet = Pet.query.get_or_404(id)
    return render_template('pet_details.html', title = 'Pet details', pet = pet)

@bp.route('/add', methods = ['GET', 'POST'])
def pet_add():
    ''' A route for showing a form and processing form for adding a new pet. '''
    
    form = AddPetForm()
    form.animal_id.choices = [(animal.id, animal.name) for animal in Animal.query.all()]

    # When the form has been submitted, process the form and save new pet to database
    if form.validate_on_submit():
        pet = Pet()
        form.populate_obj(obj=pet)
        db.session.add(pet)
        db.session.commit()
        # Return back to the view that shows the list of the user's pets
        return redirect(url_for('pet.my_pet_list'))

    # When doing a GET request or there are errors in the form, return the view with the form
    return render_template('pet_add.html', form = form, title = 'Add pet')

@bp.route('/<int:id>/edit', methods = ['GET', 'POST'])
def pet_edit(id):
    ''' A route for showing a form and processing form when editing a pet. '''
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    form.animal_id.choices = [(animal.id, animal.name) for animal in Animal.query.all()]

    # When the form has been submitted, process the form and save changes to database
    if form.validate_on_submit():
        form.populate_obj(obj=pet)
        db.session.commit()
        return redirect(url_for('pet.pet_details', id=pet.id))

    # When doing a GET request or there are errors in the form, return the view with the form
    return render_template('pet_edit.html', title = 'Pet edit', form = form, pet = pet)
