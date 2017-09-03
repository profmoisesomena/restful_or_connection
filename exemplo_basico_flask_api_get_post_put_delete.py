from flask import request, jsonify 
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

notes = {
    0: 'do the shopping',
    1: 'build the codez',
    2: 'paint the door',
}


@app.route("/", methods=['GET', 'POST','PUT','DELETE'])
def notes_list():
    """
    List or create notes.
    """
    if request.method == 'POST':
        note = request.data.get('text','')
        nova_chave = max(notes.keys()) + 1
        notes[nova_chave]=note
        return jsonify(note)
    if request.method == 'PUT':

        return "Put chamado"
    if request.method == 'DELETE':
        return "delete chamado"


    # request.method == 'GET'
    return jsonify(notes.keys(),notes.values())

app.run (debug = True, use_reloader=True)

#testando no terminal
'''
#capturando valores
curl -X GET http://127.0.0.1:5000/
#inderindo valores
curl -X POST http://127.0.0.1:5000/ -d text='Novo valor'


'''
