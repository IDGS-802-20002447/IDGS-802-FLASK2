from flask import Flask,render_template
from flask import request
from collections import Counter
import forms

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def number():
    cantidad= forms.numberF(request.form)
    if request.method=='POST':      
        sbm = request.form.get("submit")
        if sbm == 'Generar':
            return render_template('actividadForm1.html',form=cantidad)
        if sbm == 'Calcular':
            numero = request.form.getlist("numero")
           
            max = 0
            min = 0
            avg = 0
            numRepeat = ''
            
            for i in numero:
                if (max is 0 or i > max):
                    max= i
            
            for i in numero:
                if (min is 0 or i < min):
                    min = i
            for i in range(len(numero)):
                numero[i] = int(numero[i])         
        
            avg = sum(numero) / len(numero)

            count = Counter(numero)
            resul = count.most_common()
            
            for r in resul:
                if r[1] > 1:
                    numRepeat += 'El número {0} se repite {1} veces \n'.format(r[0], r[1])
                
            return render_template('resultadoAct1.html',form=cantidad, max=max, min=min,avg=avg, numRepeat = numRepeat)
    return render_template('actividadForm1.html', form=cantidad)




if __name__=="__main__":
    app.run(debug=True,port=3000)