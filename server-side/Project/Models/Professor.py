from datetime import datetime
from app import db


class Professor(db.Model):
    id = db.Column('ProfessorId', db.Integer, primary_key=True)
    cpf = db.Column('CPF', db.String(11))
    firstName = db.Column('FirstName', db.String(50))
    lastName = db.Column('LastName', db.String(50))
    birthDate = db.Column('BirthDate', db.DateTime, default=datetime.utcnow)

    def update(self):
        professor = Professor.query.filter_by(id=self.id)
        professor.cpf = self.cpf
        professor.firstName = self.firstName
        professor.lastName = self.lastName
        professor.birthDate = self.birthDate
        db.session.commit()

    def add(self):
        professor = Professor(
            cpf=self.cpf, firstName=self.firstName, lastName=self.lastName, birthDate=self.birthDate)
        db.session.add(professor)
        db.session.commit()

    def delete(self):
        professor = Professor(
            cpf=self.cpf, firstName=self.firstName, lastName=self.lastName, birthDate=self.birthDate)
        db.session.delete(professor)
        db.session.commit()
