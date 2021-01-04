from datetime import datetime
from app import db


class StudentClass(db.Model):
    id = db.Column('StudentClassId', db.Integer, primary_key=True)
    studentId = db.Column('StudentId', db.ForeignKey(
        'student.StudentId'), nullable=False)
    classId = db.Column('ClassId', db.ForeignKey(
        'class.ClassId'), nullable=False)

    def update(self):
        studentClass = StudentClass.query.filter_by(id=self.id)
        studentClass.studentId = self.studentId
        studentClass.classId = self.classId
        db.session.commit()

    def add(self):
        studentClass = StudentClass(
            studentId=self.studentId, classId=self.classId)
        db.session.add(studentClass)
        db.session.commit()

    def delete(self):
        studentClass = StudentClass(
            studentId=self.studentId, classId=self.classId)
        db.session.delete(studentClass)
        db.session.commit()
