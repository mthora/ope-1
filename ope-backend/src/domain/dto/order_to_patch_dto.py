from flask_restx import fields

OrderToPatch = {
    'id': fields.Integer(required=True),
    'done': fields.Boolean(required=True, max_length=50),

}
