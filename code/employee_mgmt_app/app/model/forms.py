from hashlib import sha256

from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, DateField, DateTimeLocalField, TextAreaField, TelField, \
    SelectField, SubmitField
from wtforms.validators import ValidationError, input_required, optional

from app.model.addresses_mgmt import get_all_addresses
from app.model.models import Employees
import app.model.employees_mgmt as employee_mgmt


class LoginForm(FlaskForm):
    email = EmailField('email')
    password = PasswordField('password')
    login = SubmitField('login')

    def validate_email(self, field):
        if field.data == '':
            raise ValidationError('Indiquer une adresse email')

    def validate_password(self, field):
        if field.data == '':
            raise ValidationError('Indiquer un mot de passe')


class TaskForm(FlaskForm):
    project = StringField('project', validators=[input_required()])
    title = StringField('title', validators=[input_required()])
    since = DateTimeLocalField('since', validators=[input_required()])
    until = DateTimeLocalField('until', validators=[input_required()])
    description = TextAreaField('description', validators=[optional()])
    submit = SubmitField('valider')


class EmployeeForm(FlaskForm):
    lastname = StringField('Nom')
    birthdate = DateField('Date de naissance')
    firstname = StringField('Prénom')
    email = EmailField('Email')
    road = StringField('Rue')
    phone_number = TelField('Numéro de téléphone')
    address_id = SelectField('Adresse', choices=[(0, '-- Choisir --')], default=0, coerce=int)
