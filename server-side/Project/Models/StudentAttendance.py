from datetime import datetime
from Enums import AttendanceStatus
from app import db


class StudentAttendance(db.Model):
    id = db.Column('StudentAttendanceId', db.Integer, primary_key=True)
    studentId = db.Column('StudentId', db.ForeignKey(
        'student.StudentId'), nullable=False)
    classId = db.Column('ClassId', db.ForeignKey(
        'class.ClassId'), nullable=False)
    date = db.Column('Date', db.DateTime, default=datetime.utcnow)
    status = db.Column('Status', db.String(
        50), default=AttendanceStatus.Undefined)
