from flask_restx import Resource, Namespace
from flask import request, jsonify, make_response
from src.domain.dto import Product_Order as Product_OrderDto
from src.domain.dto import Product_OrderToUpdate as Product_OrderToUpdateDto
from src.main.adapters import flask_adapter

from src.main.compose import create_product_order_composer
from src.main.compose import list_products_orders_composer
from src.main.compose.product_order.get_product_order_by_id_composer import get_product_order_composer
from src.main.compose.product_order.update_product_order_composer import update_product_order_composer
from src.main.compose.product_order.delete_product_order_composer import delete_product_order_composer

product_order_namespace = Namespace('products_orders')
product_order = product_order_namespace.model('Product_Order', Product_OrderDto)
product_order_update = product_order_namespace.model('Product_OrderToUpdate', Product_OrderToUpdateDto)


@product_order_namespace.route('/')

class Products_Orders(Resource):

    @product_order_namespace.expect(product_order)

    @product_order_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   500: "Internal Server Error"})
    def get(self):
        response = flask_adapter(request, list_products_orders_composer())
        return make_response(jsonify(response), int(response["status"]))

    @product_order_namespace.expect(product_order_update)
    @product_order_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   404: "Not Found",
                                   500: "Internal Server Error"})
    def put(self):
        response = flask_adapter(request, update_product_order_composer())
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

    @product_order_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   404: "Not Found",
                                   500: "Internal Server Error"})
    def delete(self, id):
        response = flask_adapter(request=request, composer=delete_product_order_composer(), arg=id)
        return make_response(jsonify(response), int(response["status"]))
