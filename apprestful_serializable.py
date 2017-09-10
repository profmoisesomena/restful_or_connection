# -*- coding: utf-8 -*-
import psycopg2
from flask import request, jsonify,render_template
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
import json

app = FlaskAPI(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/sigmap'
app.config['extend_existing']=True
db =SQLAlchemy(app)

notes = {
    0: 'do the shopping',
    1: 'build the codez',
    2: 'paint the door',
}

class cliente(db.Model):
    __tablename__ = 'cliente3'
    id = db.Column('cliente_id', db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(50))
    endereco = db.Column(db.String(255))
    telefone = db.Column(db.Integer)

    def __init__(self,nome,cidade,endereco,telefone):
        self.nome =nome
        self.cidade =cidade
        self.endereco = endereco
        self.telefone = telefone

    #serialize data to json
    @property
    def serialize_to_json(self):
        return {
        'id': self.id,
        'nome': self.nome,
        'cidade':self.cidade,
        'endereco':self.endereco,
        'telefone':self.telefone
        }

db.create_all()
#cli01 = cliente('cliente 23','nvas vitoria','rua sta alsdf asdfj',123566)
#db.session.add(cli01)
#db.session.commit()

#cli = cliente.query.all()


@app.route("/db/",methods=['GET', 'POST','PUT','DELETE'])
def retorna_dados_json_complete_object():
    if request.method == 'POST':
        #nova_chave = max(notes.keys()) + 1
        nome = request.data.get('nome','')
        cidade = request.data.get('cidade','')
        endereco = request.data.get('endereco','')
        telefone = request.data.get('telefone','')
        cli01 = cliente(nome,cidade,endereco,telefone)
        db.session.add(cli01)
        db.session.commit()
        #refresh cli01 for get new id in runtime
        db.session.refresh(cli01)
        #print cli01.id
        return jsonify(cli01.serialize_to_json)
    if request.method == 'GET':
        results = cliente.query.all()
        return jsonify(clientes=[i.serialize_to_json for i in results])

    return "API Clientes"

    
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
    return jsonify(notes)
app.run (debug = True, use_reloader=True)
