from Models import Student
from app import db


def update(updatedStudent):
    student = Student.query.filter_by(id=updatedStudent.id)
    student.cpf = updatedStudent.cpf
    student.firstName = updatedStudent.firstName
    student.lastName = updatedStudent.lastName
    student.birthDate = updatedStudent.birthDate
    db.session.commit()


def add(student):
    db.session.add(student)
    db.session.commit()


def delete(student):
    db.session.delete(student)
    db.session.commit()
