from flask import Flask, request, jsonify, json
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
from werkzeug.exceptions import HTTPException
from flask_sqlalchemy import SQLAlchemy


from Domain.StudentAttendanceDomain import StudentAttendanceDomain
from Domain.ClassDomain import ClassDomain
from Domain.ProfessorDomain import ProfessorDomain
from Domain.StudentDomain import StudentDomain

app = Flask(__name__)
app.config['TRAP_HTTP_EXCEPTIONS'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendmanager.db'

CORS(app)
api = Api(app)
db = SQLAlchemy()
db.init_app(app)


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e
    response = {
        "message": e.args[0],
        "status": 400,
    }
    return response, 400


@app.route('/')
def home():
    return "Attendance classes manager"


class StudentAttandenceController(Resource):
    def get(Self):
        return StudentAttendanceDomain().getAll(), 200

    def post(self):
        data = request.get_json()
        studentAttandenceDomain = StudentAttendanceDomain(data)
        studentAttandenceDomain.update()
        return 200


class ClassController(Resource):
    def get(self):
        return ClassDomain().getAll(), 200


class ClassByIdController(Resource):
    def get(self, classId):
        return ClassDomain().getByClassId(classId), 200


class ProfessorController(Resource):
    def get(self):
        return ProfessorDomain().getAll(), 200


class StudentController(Resource):
    def get(self, classId):
        data = request.get_json()
        return StudentDomain().getByClassId(classId), 200


api.add_resource(StudentAttandenceController, '/studentAttandence')
api.add_resource(ClassController, '/class')
api.add_resource(ClassByIdController, '/class/<int:Id>')
api.add_resource(ProfessorController, '/professor')
api.add_resource(StudentController, '/student/<int:Id>')


if __name__ == "__main__":
    app.run(port=5000, Debug=True)
