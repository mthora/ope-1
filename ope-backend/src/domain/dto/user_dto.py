from flask_restx import fields

User = {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True, max_length=50),
    'role': fields.Integer(required=True),
    'email': fields.String(required=True, max_length=100),
    'password': fields.String(required=True, max_length=100),
}
