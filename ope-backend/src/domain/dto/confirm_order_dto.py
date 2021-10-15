from flask_restx import fields

ConfirmOrder = {
    'id': fields.Integer(required=True),
    'confirmed': fields.Boolean(required=True),
}
