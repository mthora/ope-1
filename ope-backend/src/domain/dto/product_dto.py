from flask_restx import fields

Product = {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True, max_length=40),
    'description': fields.String(required=True, max_length=200),
    'category': fields.Integer(required=True),
    'price': fields.Float(required=True),
    'amount': fields.Integer(required=True),
    'promotion': fields.Boolean(Required=True),
    'img': fields.FormattedString(src_str="")
}