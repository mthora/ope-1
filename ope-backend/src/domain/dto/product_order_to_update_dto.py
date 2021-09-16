from flask_restx import fields

Product_OrderToUpdate = {
    'id': fields.Integer(required=True),
    'price': fields.Float(required=True),
    'amount': fields.Integer(required=True),
}