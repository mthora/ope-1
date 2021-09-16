from flask_restx import fields

Product_Order = {
    'id': fields.Integer(readonly=True),
    'id_product': fields.Float(required=True),
    'id_order':  fields.Float(required=True),
    'price': fields.Float(required=True),
    'amount': fields.Integer(required=True),
}