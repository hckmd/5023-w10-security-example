from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, ValidationError
from wtforms.widgets.core import HiddenInput

from app.models import Animal

class AddAnimalForm(FlaskForm):
    ''' Form for adding a new animal '''
    name = StringField('Name:', validators=[InputRequired()])
    submit = SubmitField('Add animal')

    def validate_name(form, field):
        if Animal.query.filter_by(name = field.data).first() != None:
            raise ValidationError('This animal already exists in the database.')

class EditAnimalForm(AddAnimalForm):
    ''' Form for editing an existing animal '''
    id = IntegerField(widget=HiddenInput())
    submit = SubmitField('Save changes')

    def validate_name(form, field):
        existing_animal = Animal.query.filter_by(name = field.data).first()
        if existing_animal:
            if existing_animal.id != form.id.data:
                raise ValidationError('There is already an animal with this name')
