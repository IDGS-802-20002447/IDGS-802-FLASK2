from flask import Flask,render_template
from flask import request

import forms

app=Flask(__name__)

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
    app.run(debug=True,port=3000)

