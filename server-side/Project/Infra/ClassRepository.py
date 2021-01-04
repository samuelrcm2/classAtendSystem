from Models import Class
from app import db


def update(classObject):
    classObject = Class.query.filter_by(id=classObject.id)
    classObject.professorId = classObject.professorId
    classObject.name = classObject.name
    classObject.numberOfClasses = classObject.numberOfClasses
    db.session.commit()


def add(classObject):
    db.session.add(classObject)
    db.session.commit()


def delete(classObject):
    db.session.delete(classObject)
    db.session.commit()
