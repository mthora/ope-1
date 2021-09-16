from flask_restx import fields

ProductToUpdate = {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True, max_length=50),
    'description': fields.String(required=True, max_length=200),
    'price': fields.Float(required=True),
    'amount': fields.Integer(required=True),
    'promotion': fields.Boolean(False),
    'img': fields.String(required=True, max_length=400)
}
