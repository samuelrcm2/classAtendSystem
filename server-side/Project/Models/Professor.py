from datetime import datetime
from app import db


class Professor(db.Model):
    id = db.Column('ProfessorId', db.Integer, primary_key=True)
    cpf = db.Column('CPF', db.String(11))
    firstName = db.Column('FirstName', db.String(50))
    lastName = db.Column('LastName', db.String(50))
    birthDate = db.Column('BirthDate', db.DateTime, default=datetime.utcnow)
