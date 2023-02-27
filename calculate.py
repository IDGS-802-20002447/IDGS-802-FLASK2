from flask import Flask, render_template, request, flash, make_response
from collections import namedtuple
from flask_wtf.csrf import CSRFProtect
from flask import flash
import forms
app = Flask(__name__)

app.config['SECRET_KEY']="Esta es una clave encriptada"
csrf=CSRFProtect()


colors = {
    'black': 'Negro',
    'brown': 'Café',
    'red': 'Rojo',
    'orange': 'Naranja',
    'yellow': 'Amarillo',
    'green': 'Verde',
    'blue': 'Azul',
    'purple': 'Morado',
    'gray': 'Gris',
    'white': 'Blanco',
    'gold': 'Dorado',
    'silver': 'Plateado'
}

@app.route('/', methods=['GET', 'POST'])
def resistenciaForm():
    form = forms.ResistanceForm(request.form)

    if request.method == 'POST' and form.validate():
        user=form.username.data
        bandA_color = form.band_A.data
        bandA_num = bandNum(bandA_color)
        bandB_color = form.band_B.data
        bandB_num = bandNum(bandB_color)
        bandC_color = form.band_C.data
        bandC_num = bandNum(bandC_color)
        bandD_color = form.band_D.data
        bandD_num = bandNum(bandD_color)
        
        
        bandA_nom = colors[bandA_color]
        bandB_nom = colors[bandB_color]
        bandC_nom = colors[bandC_color]
        bandD_nom = colors[bandD_color]

        resisitencia = (bandA_num * 10 + bandB_num) * 10 ** bandC_num
        
        tolerancia = 'Plateado' if bandD_num == 'silver' else 'Dorado'
        resMin = resisitencia * 0.95
        resMax = resisitencia * 1.05
        result = namedtuple('ResResult', ['min', 'value', 'tolerancia','max'])
        result.value = resisitencia
        result.tolerancia = tolerancia
        result.min=resMin
        result.max=resMax
        succes_message="Gracias por usar nuestra calculadora {} espero te haya servido la informacion.".format(user)
        flash(succes_message)

        response = make_response(render_template('calculate.html', form=form, result=result, 
                                                  bandA_color=bandA_color, bandA_nom=bandA_nom,
                                                  bandB_color=bandB_color, bandB_nom=bandB_nom,
                                                  bandC_color=bandC_color, bandC_nom=bandC_nom,
                                                  bandD_color=bandD_color,bandD_nom=bandD_nom,
                                                  tolerancia=tolerancia,user=user,
                                                  resMin=resMin,
                                                  resMax=resMax
                                                  ))
        response.set_cookie('bandA_color', bandA_color)
        response.set_cookie('bandB_color', bandB_color)
        response.set_cookie('bandC_color', bandC_color)
        response.set_cookie('tolerancia', tolerancia)
        
        
        return response
    
    return render_template('calculate.html', form=form)


def bandNum(color):
    bandas = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 
             'purple': 7, 'gray': 8, 'white': 9, 'gold': -1, 'silver': -2}
    return bandas[color]


if __name__=="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)
