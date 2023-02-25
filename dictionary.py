import forms
from flask import Flask, render_template, request
from wtforms import Form, StringField, validators, RadioField


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dictionary():
    dictionary_file = 'dictionary.txt'
    words = {}
    if request.method == 'POST':
        sbm = request.form.get("submit")

        add_form = forms.DictionaryForm(request.form)
        search_form = forms.SearchForm(request.form)
        success = False

        if sbm == 'Agregar' and add_form.validate():
            english_word = add_form.english_word.data.lower()
            spanish_word = add_form.spanish_word.data.lower()

            with open(dictionary_file, 'a') as f:
                f.write(f'{english_word}:{spanish_word}\n')

            add_form = forms.DictionaryForm()
            success = True

        results = []
        
        if sbm == 'Buscar' and search_form.validate():
            search_term = search_form.search_term.data
            search_language = search_form.search_language.data
            print(f"Buscando '{search_term}' en el idioma '{search_language}'")
            with open('dictionary.txt', 'r') as f:
                for line in f:
                    english_word, spanish_word = line.strip().split(':')
                    if search_language == 'english' and search_term.lower() in english_word.lower():
                        results.append({'english': english_word, 'spanish': spanish_word})
                    if search_language == 'spanish' and search_term.lower() in spanish_word.lower():
                        results.append({'english': english_word, 'spanish': spanish_word})
                if len(results) == 0:
                    no_results = True

            print(f"Resultados: {results}")



        with open(dictionary_file, 'r') as f:
            for line in f:
                english_word, spanish_word = line.strip().split(':')
                words[english_word] = spanish_word

        return render_template('diccionario.html', add_form=add_form, search_form=search_form, words=words, success=success, results=results)

    else:
        add_form = forms.DictionaryForm()
        search_form = forms.SearchForm()
        with open(dictionary_file, 'r') as f:
            for line in f:
                english_word, spanish_word = line.strip().split(':')
                words[english_word] = spanish_word

        return render_template('diccionario.html', add_form=add_form, search_form=search_form, words=words, success=False)


if __name__=="__main__":
    app.run(debug=True,port=3000)

