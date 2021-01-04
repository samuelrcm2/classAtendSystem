from datetime import datetime
from app import db


class Class(db.Model):
    id = db.Column('ClassId', db.Integer, primary_key=True)
    professorId = db.Column('IdProfessor', db.ForeignKey(
        'professor.ProfessorId'), nullable=False)
    name = db.Column('Nome', db.String(50))
    numberOfClasses = db.Column('NumeroDeAulas', db.Integer)

    def update(self):
        classObject = Class.query.filter_by(id=self.id)
        classObject.professorId = self.professorId
        classObject.name = self.name
        classObject.numberOfClasses = self.numberOfClasses
        db.session.commit()

    def add(self):
        classObject = Class(
            professorId=self.professorId, name=self.name, numberOfClasses=self.numberOfClasses)
        db.session.add(classObject)
        db.session.commit()

    def delete(self):
        classObject = Class(
            professorId=self.professorId, name=self.name, numberOfClasses=self.numberOfClasses)
        db.session.delete(classObject)
        db.session.commit()
