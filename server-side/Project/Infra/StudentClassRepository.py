from Models import StudentClass
from app import db


def update(updatedStudentClass):
    studentClass = StudentClass.query.filter_by(id=updatedStudentClass.id)
    studentClass.studentId = updatedStudentClass.studentId
    studentClass.classId = updatedStudentClass.classId
    db.session.commit()


def add(studentClass):
    db.session.add(studentClass)
    db.session.commit()


def delete(studentClass):
    db.session.delete(studentClass)
    db.session.commit()


def getByClassId(classId):
    return StudentClass.query.filter_by(id=classId)
