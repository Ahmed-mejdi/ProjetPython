from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base  # noqa
from fastapi_users.db import SQLAlchemyBaseUserTable

# Table d'association many-to-many entre Etudiant et Formation
etudiant_formation = Table(
    'etudiant_formation',
    Base.metadata,
    Column('etudiant_id', Integer, ForeignKey('etudiants.id'), primary_key=True),
    Column('formation_id', Integer, ForeignKey('formations.id'), primary_key=True)
)

class Departement(Base):
    __tablename__ = 'departements'
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=True, nullable=False)
    description = Column(String)
    etudiants = relationship('Etudiant', back_populates='departement')

class Formation(Base):
    __tablename__ = 'formations'
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, nullable=False)
    description = Column(String)
    theme = Column(String)
    duree = Column(Integer)
    etudiants = relationship('Etudiant', secondary=etudiant_formation, back_populates='formations')

class Etudiant(Base):
    __tablename__ = 'etudiants'
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    mot_de_passe = Column(String, nullable=False)
    departement_id = Column(Integer, ForeignKey('departements.id'))
    departement = relationship('Departement', back_populates='etudiants')
    formations = relationship('Formation', secondary=etudiant_formation, back_populates='etudiants')

class User(SQLAlchemyBaseUserTable, Base):
    nom = Column(String, nullable=False)
    departement_id = Column(Integer, ForeignKey('departements.id'))
    departement = relationship('Departement')
