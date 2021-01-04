from datetime import datetime
from app import db


class StudentClass(db.Model):
    id = db.Column('StudentClassId', db.Integer, primary_key=True)
    studentId = db.Column('StudentId', db.ForeignKey(
        'student.StudentId'), nullable=False)
    classId = db.Column('ClassId', db.ForeignKey(
        'class.ClassId'), nullable=False)
