import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True) 
    firstName = Column(String(250))
    lastName = Column(String(250))
    email = Column(String(250)) 

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    age = Column(Integer)
    description = Column(String(250))
    favorite_id = Column(Integer, ForeignKey('favorite.id'))

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    capital = Column(String(250))
    description = Column(String(250))
    favorite_id = Column(Integer, ForeignKey('favorite.id'))

class Favorite(Base):  
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User) 
    character = relationship('Characters', back_populates="favorite") 
    planet = relationship('Planets', back_populates="favorite")
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')