# coding: utf-8
#!pip install Flask-MongoAlchemy
from flask.ext.mongoalchemy import MongoAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pprint
app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'sigmap'
#pprint.pprint(app.config)
db = MongoAlchemy(app)
class cliente(db.Document):
   codigo = db.IntField()
   nome = db.StringField()
   cidade = db.StringField()
#cliente1 = cliente(nome='cliente1')
dados_cliente = cliente(codigo=1, nome='cliente1', cidade='serra')
dados_cliente.save()
# References:
# https://pythonhosted.org/Flask-MongoAlchemy/
