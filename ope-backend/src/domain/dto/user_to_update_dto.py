from flask_restx import fields

UserToUpdate = {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True, max_length=50),
    'role': fields.Integer(required=True),
    'email': fields.String(required=True, max_length=100)
}
