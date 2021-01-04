from Models import Student
from Infra import StudentClassRepository
from app import db


def getByClassId(self, classId):
    studentClassData = StudentClassRepository.getByClassId(classId)
    return db.session.query(Student).filter_by(Student.id.in_(map(lambda x: x.studentId, studentClassData)))


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
