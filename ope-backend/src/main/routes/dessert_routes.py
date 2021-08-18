from flask_restx import Resource, Namespace
from flask import request, jsonify, make_response
from src.domain.dto import Dessert as DessertDto
from src.main.adapters import flask_adapter

from src.main.compose import create_dessert_composer

dessert_namespace = Namespace('desserts')
dessert = dessert_namespace.model('Dessert', DessertDto)


@dessert_namespace.route('/')
class Dessert(Resource):
    @dessert_namespace.expect(dessert)
    @dessert_namespace.doc(responses={201: 'Created',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   500: "Internal Server Error"})
    def post(self):
        response = flask_adapter(request, create_dessert_composer())
        return make_response(jsonify(response), int(response['status']))