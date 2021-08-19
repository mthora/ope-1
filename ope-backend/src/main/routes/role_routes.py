from flask_restx import Resource, Namespace
from flask import request, jsonify, make_response
from src.domain.dto import Roles as RolesDto
from src.main.adapters import flask_adapter

from src.main.compose import create_role_composer

role_namespace = Namespace('role')
role = role_namespace.model('Role', RolesDto)

@role_namespace.route('/')
class Drinks(Resource):
    @role_namespace.expect(role)
    @role_namespace.doc(responses={201: 'Created',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   500: "Internal Server Error"})
    def post(self):
        response = flask_adapter(request, create_role_composer())
        return make_response(jsonify(response), int(response["status"]))