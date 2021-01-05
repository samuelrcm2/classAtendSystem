from datetime import datetime
from Models.Base import db


class Student(db.Model):
    id = db.Column('StudentId', db.Integer, primary_key=True)
    cpf = db.Column('CPF', db.String(11))
    firstName = db.Column('FirstName', db.String(50))
    lastName = db.Column('LastName', db.String(50))
    birthDate = db.Column('BirthDate', db.DateTime, default=datetime.utcnow)
