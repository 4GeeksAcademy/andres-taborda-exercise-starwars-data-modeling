
import enum
import os
import sys
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    favorites = relationship('Favorite', back_populates='user')


class Favorite(Base):
    __tablename__ = 'favorites'

    favorite_id = Column(Integer, primary_key=True)  
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  
    type = Column(Enum("planet","character"), nullable=False)  

    user = relationship('User', back_populates='favorites')

    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    planet = relationship('Planet', back_populates='favorites')

    
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    character = relationship('Character', back_populates='favorites')

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    height = Column(Integer)
    skin_color = Column(String(50))
    species = Column(String(50))
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship('Planet', back_populates='characters')
    favorites = relationship('Favorite', back_populates='planet')

class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(100))
    population = Column(Integer)
    terrain = Column(String(100))
    characters = relationship('Character', back_populates='homeworld')
    favorites = relationship('Favorite', back_populates='planet')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
