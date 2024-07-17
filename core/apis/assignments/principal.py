from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from .schema import AssignmentSchema, TeacherSchema, AssignmentGradeSchema
from core.models.assignments import Assignment
from core.models.teachers import Teacher


principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments for principal"""
    submitted_graded_assignments = Assignment.get_submitted_and_graded_assignments()
    submitted_graded_assignments = AssignmentSchema().dump(submitted_graded_assignments, many=True)
    return APIResponse.respond(data=submitted_graded_assignments)

#get all the teachers
@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of teachers"""
    teachers = Teacher.get_teachers()
    teachers = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teachers)

#grade an assignment
@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)