# models.py

"""Models for Pet."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = 'tablePet'

    id= db.Column(db.Integer,nullable= False, primary_key=True, autoincrement=True)
    name=  db.Column(db.Text, nullable=False, unique=True)
    species= db.Column(db.Text, nullable=False)
    photo_url=db.Column(db.Text, nullable=True, unique=False)
    age=db.Column(db.Integer,nullable=True)
    notes=db.Column(db.Text, nullable=True)
    available= db.Column(db.Boolean, nullable=False, default=True)

    