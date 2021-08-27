from flask_restx import fields

Order = {
    'id': fields.Integer(readonly=True),
    'done': fields.Boolean(required=True),
    'initial_date': fields.String(required=True, max_length=20),
    'end_date': fields.String(required=False, max_length=20),
    'consumed_in': fields.String(required=True, max_length=20),
    'table': fields.Integer(required=True),
    'payment_method': fields.String(required=True, max_length=20),
    'obs': fields.String(required=True, max_length=200),
    'confirmed': fields.Boolean(required=True)
}
