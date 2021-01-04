from Models import StudentAttendance
from app import db


def getAll():
    return StudentAttendance.query.all()


def update(studentAttendance):
    studentAttendance = StudentAttendance.query.filter_by(
        id=studentAttendance.id).update(dict(status=studentAttendance.status))
    db.session.commit()


def add(studentAttendance):
    db.session.add(studentAttendance)
    db.session.commit()
