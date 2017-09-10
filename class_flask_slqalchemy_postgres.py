
# coding: utf-8
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pprint
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/sigmap'
app.config['extend_existing']=True
#pprint.pprint(app.config)
db =SQLAlchemy(app)
class cliente(db.Model):
   id = db.Column('cliente_id', db.Integer, primary_key = True)
   nome = db.Column(db.String(100))
   cidade = db.Column(db.String(50))
   endereco = db.Column(db.String(200))
   telefone = db.Column(db.Integer)
def __init__(self, nome,cidade,endereco):
    self.nome =nome
    self.cidade =cidade
    self.endereco = endereco
    self.telefone = telefone
db.create_all()
cli = cliente.query.filter_by(nome = 'cliente1').all()
'''
for i in cli:
    print(i.id)
    print(i.nome)
    print(i.cidade)
    print(i.telefone)
'''
