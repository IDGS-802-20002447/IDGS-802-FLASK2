from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,SubmitField,FieldList,FormField,SelectField,RadioField,EmailField
from wtforms.fields  import EmailField,TextAreaField,PasswordField
from wtforms import validators



class UserForm(Form):

    matricula=StringField('Matricula',[ validators.DataRequired(message='La matricula es requerida')
                                     ])
    nombre=StringField('Nombre',[ validators.DataRequired(message='El campo es requerido'),
                                validators.length(min=5,max=15,message="Ingrese un valor maximo")])
    apePaterno=StringField('ApePaterno')
    apeMatermo=StringField('ApeMaterno')
    email=EmailField('Correo')





#Clase de la actividad 1
class numberF(Form):
    numEntrada = IntegerField('Numero de campos', [validators.DataRequired(message='Indica el numero de campos que deseas')])
    numero = IntegerField('numero')