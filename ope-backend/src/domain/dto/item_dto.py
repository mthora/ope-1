from flask_restx import fields

Item = {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True, max_length=40),
    'description': fields.String(required=True, max_length=200),
    'price': fields.Float(required=True),
    'amount': fields.Integer(required=True),
    'promotion': fields.Boolean(required=False),
    'img': fields.String(required=True, max_length=400)
}

