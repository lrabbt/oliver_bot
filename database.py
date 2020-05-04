from sqlalchemy import create_engine
import logging
from sqlalchemy.orm import sessionmaker, session
from pymongo import MongoClient
import pprint
from os import environ
from model import Base, Questions
import sqlite3

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

client = MongoClient('mongodb+srv://marcobacelo:61286539382420832782@cluster0-ktov0.mongodb.net/test?retryWrites=true&w=majority')
db = client['questions']
collection = db['questions']


new_question = [{"question": "Quais as cores disponives?", "answer": "Roxo e Vermelho", "key_word": "cor"},
        {"question": "Qual o tamanho?", "answer": "Grande", "key_word": "tamanho"}]

question = collection
question_id = question.insert_many(new_question)
question_id.inserted_ids

pprint.pprint(question.find_one({"key_word": "tamanho"}))
pprint.pprint(question.find_one({"key_word": "cor"}))


#engine = create_engine('postgres://user:user_password@postgrees_database:5432/database')

# Create All Tables
#Base.metadata.create_all(engine)

#newQuestion = Questions(question='Qual a cor?', answer='Vermelho, Azul', key_word='cor')

#Session = sessionmaker()
#Session.configure(bind=engine)
#session = Session()
#session.add(newQuestion)
#session.commit()

