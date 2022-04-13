from flask_wtf import FlaskForm
from wtforms import validators, StringField, DateTimeLocalField, TextAreaField
from wtforms.validators import InputRequired


class TaskForm(FlaskForm):
    project = StringField('project', validators=[InputRequired(), validators.EqualTo('Indiquer une nom de projet')])
    title = StringField('title', validators=[InputRequired(), validators.EqualTo('Indiquer un titre pour la tâche')])
    since = StringField('since', validators=[InputRequired(), validators.EqualTo('Indiquer une heure et une date de début')])
    until = StringField('until', validators=[InputRequired(), validators.EqualTo('Indiquer une nom de projet')])
    description = StringField('description', validators=[InputRequired(), validators.EqualTo('Indiquer une nom de projet')])