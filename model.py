from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer,
                primary_key=True)
    question = Column(String(90),
                      nullable=False)
    answer = Column(String(90),
                    nullable=False)
    key_word = Column(String(90),
                      nullable=False)


    def __init__(self, question, answer, key_word):
        self.question = question
        self.answer = answer
        self.key_word = key_word


    def __repr__(self):
        return "<Questions('%s', '%s', '%s')>" % (
            self.question, self.answer, self.key_word)
