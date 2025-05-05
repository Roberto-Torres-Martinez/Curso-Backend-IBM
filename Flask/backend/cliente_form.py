from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields.simple import StringField, SubmitField, HiddenField
from wtforms.fields.numeric import IntegerField

class ClienteForm(FlaskForm):
    id = HiddenField('id')
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    membresia = IntegerField('Membresia', validators=[DataRequired()])
    guardar = SubmitField('Guardar')