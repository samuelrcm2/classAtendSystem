from datetime import datetime
from app import db


class Student(db.Model):
    id = db.Column('StudentId', db.Integer, primary_key=True)
    cpf = db.Column('CPF', db.String(11))
    firstName = db.Column('FirstName', db.String(50))
    lastName = db.Column('LastName', db.String(50))
    birthDate = db.Column('BirthDate', db.DateTime, default=datetime.utcnow)

    def update(self):
        student = Student.query.filter_by(id=self.id)
        student.cpf = self.cpf
        student.firstName = self.firstName
        student.lastName = self.lastName
        student.birthDate = self.birthDate
        db.session.commit()

    def add(self):
        student = Student(
            cpf=self.cpf, firstName=self.firstName, lastName=self.lastName, birthDate=self.birthDate)
        db.session.add(student)
        db.session.commit()

    def delete(self):
        student = Student(
            cpf=self.cpf, firstName=self.firstName, lastName=self.lastName, birthDate=self.birthDate)
        db.session.delete(student)
        db.session.commit()
