from flask_restx import Resource, Namespace
from flask import request, jsonify, make_response
from src.main.adapters import flask_adapter

from src.main.compose.product_order.get_product_order_by_id_composer import get_product_order_composer
from src.main.compose import list_products_orders_composer

product_order_namespace = Namespace('products_orders')


@product_order_namespace.route('/')

class Products_Orders(Resource):

    @product_order_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   500: "Internal Server Error"})
    def get(self):
        response = flask_adapter(request, list_products_orders_composer())
        return make_response(jsonify(response), int(response["status"]))


@product_order_namespace.route('/<int:id>', endpoint='products_orders')
@product_order_namespace.doc(params={"id": 'Id do Product Order'})


class Product_OrderActions(Resource):
    @product_order_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   404: "Not Found",
                                   500: "Internal Server Error"})
    def get(self, id):
        response = flask_adapter(request=request, composer=get_product_order_composer(), arg=id)
        return make_response(jsonify(response), int(response["status"]))
