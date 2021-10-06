from flask_restx import Resource, Namespace
from flask import request, jsonify, make_response
from src.domain.dto import Order as OrderDto
from src.main.adapters import flask_adapter
from src.domain.dto import OrderToPatch as OrderToPatchDto

from src.main.compose import create_order_composer
from src.main.compose import list_orders_composer
from src.main.compose.order.get_order_by_id_composer import get_order_composer
from src.main.compose.order.patch_order_composer import patch_order_composer

order_namespace = Namespace('orders')
order = order_namespace.model('Order', OrderDto)
order_patch = order_namespace.model('OrderToPatch', OrderToPatchDto)


@order_namespace.route('/')
class Orders(Resource):

    @order_namespace.expect(order)
    @order_namespace.doc(responses={201: 'Created',
                                    400: 'Bad Request',
                                    409: 'Integrity Error',
                                    500: 'Internal Server Error'})
    def post(self):
        response = flask_adapter(request, create_order_composer())
        return make_response(jsonify(response), int(response["status"]))

    @order_namespace.doc(responses={200: 'OK',
                                    400: 'Bad Request',
                                    409: "Integrity Error",
                                    500: "Internal Server Error"})
    def get(self):
        response = flask_adapter(request, list_orders_composer())
        return make_response(jsonify(response), int(response["status"]))


    @order_namespace.expect(order_patch)
    @order_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   404: "Not Found",
                                   500: "Internal Server Error"})
    def put(self):
        response = flask_adapter(request, patch_order_composer())
        return make_response(jsonify(response), int(response["status"]))


@order_namespace.route('/<int:id>', endpoint='orders')
@order_namespace.doc(params={"id": 'Order Id'})
class OrderActions(Resource):
    @order_namespace.doc(responses={200: 'OK',
                                    400: 'Bad Request',
                                    409: "Integrity Error",
                                    404: "Not Found",
                                    500: "Internal Server Error"})
    def get(self, id):
        response = flask_adapter(request=request, composer=get_order_composer(), arg=id)
        return make_response(jsonify(response), int(response["status"]))


