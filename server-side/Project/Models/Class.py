from datetime import datetime
from Models.Base import db


class Class(db.Model):
    id = db.Column('ClassId', db.Integer, primary_key=True)
    professorId = db.Column('IdProfessor', db.ForeignKey(
        'professor.ProfessorId'), nullable=False)
    name = db.Column('Nome', db.String(50))
    numberOfClasses = db.Column('NumeroDeAulas', db.Integer)
