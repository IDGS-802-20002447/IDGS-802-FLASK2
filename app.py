from flask import Flask,render_template
from flask import request
#Para trabajar con la validacion del token
from flask_wtf.csrf import CSRFProtect
#Para trabajar on las cookies(Se trabajan co RESPONSE)
#Mensajes flash tienen sist de almacenamiento
from flask import flash
from flask import make_response
import forms


#csrf nos genera un token
app=Flask(__name__)
app.config['SECRET_KEY']="Esta es una clave encriptada"
csrf=CSRFProtect()

#cuando mande llamar a una ruta que no
@app.errorhandler(404)
def no_encotrada(e):
    return render_template("404.html"),404


#cuando mande llamar a cookie primero llegara a before despues a cookie
@app.before_request
def before_request():
    print("numero1")

@app.route("/cookies",methods=["GET","POST"])
def cookies():
    print("numero2")
    reg_user=forms.LoginForm(request.form)
    datos=""
    if request.method=="POST" and reg_user.validate():
        user=reg_user.username.data
        passw=reg_user.password.data
        datos=user+"@"+passw
        succes_message="Bienvenido {}".format(user)
        flash(succes_message)

    response=make_response(render_template("cookies.html",form=reg_user))
    response.set_cookie("dato_user",datos)

    return response
# Se regresa un response no el return    return render_template("cookies.html",form=reg_user)


@app.after_request
def after_request(response):
    print("numero3")
    return response

@app.route("/saludo")
def saludo():
    valor_cookie=request.cookies.get("dato_user")
    nombre=valor_cookie.split('@')
    return render_template("saludo.html",nom=nombre[0])


@app.route("/formulario2",methods=["GET"])
def formulario2():
    return render_template("formulario2.html")

@app.route("/Alumnos",methods=['GET','POST'])
def Alumno():
    alum_form=forms.UserForm(request.form)
    mat=''
    nom=''
    if request.method=='POST' and alum_form.validate():
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)
        #alum_form=forms.apePaterno.data
        #alum_form=forms.apeMaterno.data
        #alum_form=forms.email.data
    return render_template("Alumnos.html",form=alum_form,mat=alum_form.matricula,nom=alum_form.nombre) 


if __name__=="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)

