from flask_restx import Resource, Namespace
from flask import request, jsonify, make_response
from src.domain.dto import Drinks as DrinkDto
from src.main.adapters import flask_adapter

from src.main.compose import create_drink_composer
from src.main.compose import list_drinks_composer
from src.main.compose.drink.get_drink_by_id_composer import get_drink_composer


drink_namespace = Namespace('drinks')
drink = drink_namespace.model('Drink', DrinkDto)

@drink_namespace.route('/')
class Drinks(Resource):
    @drink_namespace.expect(drink)
    @drink_namespace.doc(responses={201: 'Created',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   500: "Internal Server Error"})
    def post(self):
        response = flask_adapter(request, create_drink_composer())
        return make_response(jsonify(response), int(response["status"]))

    @drink_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   500: "Internal Server Error"})
    def get(self):
        response = flask_adapter(request, list_drinks_composer())
        return make_response(jsonify(response), int(response["status"]))


@drink_namespace.route('/<int:id>', endpoint='drinks')
@drink_namespace.doc(params={"id": 'Id da bebida'})
class DrinkActions(Resource):
    @drink_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   404: "Not Found",
                                   500: "Internal Server Error"})
    def get(self, id):
        response = flask_adapter(request=request, composer=get_drink_composer(), arg=id)
        return make_response(jsonify(response), int(response["status"]))
