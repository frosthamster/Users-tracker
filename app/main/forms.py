from functools import wraps
from itertools import chain

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, RadioField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length
from string import capwords
from app.models import User


def args_not_none(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if any(a is None for a in chain(args, kwargs.values())):
            return None
        return f(*args, **kwargs)

    return wrapper


@args_not_none
def normalize_full_name(full_name):
    return capwords(full_name)


@args_not_none
def normalize_other_pet(pet):
    return ' '.join(pet.split()).lower()


class AddingUserForm(FlaskForm):
    full_name = StringField('Full name',
                            validators=[DataRequired(),
                                        Length(max=90)],
                            filters=[normalize_full_name],
                            render_kw={'placeholder': 'Anisimov Danil Alekseevich'})

    birthday = DateField('Birthday', format='%d.%m.%Y', render_kw={'placeholder': 'DD.MM.YYYY'})

    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])

    pet = SelectField('Pet', validators=[DataRequired()],
                      choices=[('none', "No pets"), ('cat', 'Cat'),
                               ('dog', 'Dog'), ('parrot', 'Parrot'), ('other', 'Other')])

    other_pet = StringField('Other pet', validators=[Length(max=60)],
                            filters=[normalize_other_pet],
                            render_kw={'placeholder': 'Other pet'})
    submit = SubmitField('Add user')

    @property
    def name_parts(self):
        return self.full_name.data.split()

    def validate_full_name(self, full_name):
        if len(full_name.data.split()) != 3:
            raise ValidationError('Enter full name in format: last_name first_name middle_name')

    def validate_other_pet(self, other_pet):
        if self.pet.data == 'other' and not other_pet.data:
            raise ValidationError('Enter other pet')
