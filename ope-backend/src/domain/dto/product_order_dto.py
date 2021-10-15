from flask_restx import fields

Product_Order = {
    'id': fields.Integer(readonly=True),
    'product_id': fields.Integer(required=True),
    'order_id':  fields.Integer(required=True),
    'price': fields.Float(required=True),
    'amount': fields.Integer(required=True),
}