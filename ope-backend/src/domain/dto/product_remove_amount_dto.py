from flask_restx import fields

ProductRemoveAmount = {
    'id': fields.Integer(required=True),
    'amount_to_remove': fields.Integer(required=True),
}