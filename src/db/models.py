from sqlalchemy import Column, Integer, String, Float

from db.database import  base



class Words(base):
    __tablename__ = "words"

    name = Column(String, primary_key = True)


class OverlapWords(base):
    __tablename__ = "overlapwords"

    name = Column(String, primary_key=True)


class SelectWords(base):
    __tablename__ = "selectwords"

    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String)
    overlap = Column(Integer)


class FirstWord(base):
    __tablename__ = "firstword"

    name = Column(String, primary_key=True)


class Results(base):
    __tablename__ = "results"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    how_much = Column(Integer)
    timer = Column(Float)