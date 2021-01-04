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

    def update(self):
        studentAttendance = StudentAttendance.query.filter_by(id=self.id).update(dict(status=self.status)))
        db.session.commit()

    def add(self):
        studentAttendance=StudentAttendance(
            studentId = self.studentId, classId = self.classId, date = self.date, status = self.status)
        db.session.add(studentAttendance)
        db.session.commit()
