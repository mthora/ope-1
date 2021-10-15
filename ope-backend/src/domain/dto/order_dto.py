from flask_restx import fields

Order = {
    'id': fields.Integer(readonly=True),
    'consumed_in': fields.Integer(required=True),
    'table': fields.Integer(required=False),
    'payment_method': fields.Integer(required=True),
    'obs': fields.String(required=False, max_length=200)
}
