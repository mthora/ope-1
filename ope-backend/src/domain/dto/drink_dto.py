from flask_restx import fields

Drinks = {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True, max_length=40),
    'price': fields.Float(required=True),
    'amount': fields.Integer(required=True),
    'img': fields.String(required=True, max_length=400)}