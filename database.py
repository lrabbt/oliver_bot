from sqlalchemy import create_engine
import logging
from sqlalchemy.orm import sessionmaker, session
from os import environ
from model import Base, Questions
import sqlite3

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Create engine
#engine = create_engine('mysql+mysqldb://root:root@mysql_database:3306/database')

engine = create_engine('postgres://user:user_password@postgrees_database:5432/database')

# Create All Tables
Base.metadata.create_all(engine)

newQuestion = Questions(question='Qual a cor?', answer='Vermelho, Azul', key_word='cor')

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
session.add(newQuestion)
session.commit()

