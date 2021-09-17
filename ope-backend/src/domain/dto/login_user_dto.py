from flask_restx import fields

LoginUser = {
    'email': fields.String(required=True, max_length=100),
    'password': fields.String(required=True, max_length=100)
}