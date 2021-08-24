from flask_restx import Resource, Namespace
from flask import request, jsonify, make_response
from src.domain.dto import Item as ItemDto
from src.main.adapters import flask_adapter

from src.main.compose import create_item_composer
from src.main.compose import list_item_composer

item_namespace = Namespace('itens')
item = item_namespace.model('Item', ItemDto)


@item_namespace.route('/')
class Item(Resource):
    @item_namespace.expect(item)
    @item_namespace.doc(responses={201: 'Created',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   500: "Internal Server Error"})
    def post(self):
        response = flask_adapter(request, create_item_composer())
        return make_response(jsonify(response), int(response['status']))

    @item_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   500: "Internal Server Error"})
    def get(self):
        response = flask_adapter(request, list_item_composer())
        return make_response(jsonify(response), int(response["status"]))
