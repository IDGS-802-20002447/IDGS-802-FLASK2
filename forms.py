from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,SubmitField,FieldList,FormField,SelectField,RadioField,EmailField
from wtforms.fields  import EmailField,TextAreaField,PasswordField
from wtforms import validators

#Se realiaza un metodo de una validaion 
def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError("El campo no tiene datos")



class UserForm(Form):

    matricula=StringField('Matricula',[ validators.DataRequired(message='La matricula es requerida')])
    nombre=StringField('Nombre',[ validators.DataRequired(message='El campo es requerido'),
                                validators.length(min=5,max=15,message="Ingrese un valor maximo")])
    apePaterno=StringField('ApePaterno',[mi_validacion])
    apeMatermo=StringField('ApeMaterno')
    email=EmailField('Correo')


#Clase de la actividad en clase 25/02/2023

class LoginForm(Form):
    username=StringField('Usuario',[ validators.DataRequired(message='El usuario es requerido')])
    password=PasswordField('contraseña',[ validators.DataRequired(message='El campo es requerido'),
                                validators.length(min=5,max=15,message="Ingrese un valor maximo")])
 


#Clase de la actividad 1
class numberF(Form):
    numEntrada = IntegerField('Numero de campos', [validators.DataRequired(message='Indica el numero de campos que deseas')])
    numero = IntegerField('numero')




#Clase de la actividad 2
class DictionaryForm(Form):
    english_word = StringField('Palabra en inglés', [validators.DataRequired(message='La palabra es requerida')])
    spanish_word = StringField('Palabra en español', [validators.DataRequired(message='La palabra es requerida')])


class SearchForm(Form):
    search_term = StringField('Palabra', [validators.DataRequired(message='La palabra es requerida')])
    search_language = RadioField('Idioma', choices=[('english', 'Inglés'), ('spanish', 'Español')],
                                 validators=[validators.InputRequired(message='Selecciona una de las opciones')], default='english')