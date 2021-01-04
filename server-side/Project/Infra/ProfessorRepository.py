from Models import Professor
from app import db


def update(updatedProfessor):
    professor = Professor.query.filter_by(id=updatedProfessor.id)
    professor.cpf = updatedProfessor.cpf
    professor.firstName = updatedProfessor.firstName
    professor.lastName = updatedProfessor.lastName
    professor.birthDate = updatedProfessor.birthDate
    db.session.commit()


def add(professor):
    db.session.add(professor)
    db.session.commit()


def delete(professor):
    db.session.delete(professor)
    db.session.commit()
