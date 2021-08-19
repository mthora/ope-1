from flask_restx import fields

Roles = {
    'id': fields.Integer(reandoly=True),
    'role': fields.String(required=True, max_length=20)
}
