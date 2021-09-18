from flask_restx import Resource, Namespace
from flask import request, jsonify, make_response
from src.domain.dto import Product as ProductDto
from src.main.adapters import flask_adapter
from src.domain.dto import ProductToUpdate as ProductToUpdateDto
from src.main.utils import admin_route


from src.main.compose import create_product_composer
from src.main.compose import list_products_composer
from src.main.compose.product.delete_product_composer import delete_product_composer
from src.main.compose.product.update_product_composer import update_product_composer

product_namespace = Namespace('products')
product = product_namespace.model('Product', ProductDto)
product_update = product_namespace.model('ProductToUpdate', ProductToUpdateDto)
parser = product_namespace.parser()
parser.add_argument('Authorization', location='headers')


@product_namespace.route('/')
@product_namespace.expect(parser)
class Products(Resource):
    @product_namespace.expect(product)
    @product_namespace.doc(responses={201: 'Created',
                                      400: 'Bad Request',
                                      409: "Integrity Error",
                                      500: "Internal Server Error"})
    def post(self):
        try:
            admin_route(request)
        except:
            return make_response(jsonify({"data": "Usuário não autorizado"}), 401)
        response = flask_adapter(request, create_product_composer())
        return make_response(jsonify(response), int(response['status']))

    @product_namespace.doc(responses={200: 'OK',
                                      400: 'Bad Request',
                                      409: "Integrity Error",
                                      500: "Internal Server Error"})
    def get(self):
        try:
            admin_route(request)
        except:
            return make_response(jsonify({"data": "Usuário não autorizado"}), 401)
        response = flask_adapter(request, list_products_composer())
        return make_response(jsonify(response), int(response["status"]))

    @product_namespace.expect(product_update)
    @product_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   404: "Not Found",
                                   500: "Internal Server Error"})
    def put(self):
        try:
            admin_route(request)
        except:
            return make_response(jsonify({"data": "Usuário não autorizado"}), 401)
        response = flask_adapter(request, update_product_composer())
        return make_response(jsonify(response), int(response["status"]))


@product_namespace.route('/<int:id>', endpoint='products')
@product_namespace.doc(params={"id": "Id do produto"})
@product_namespace.expect(parser)
class ProductActions(Resource):
    @product_namespace.doc(responses={200: 'OK',
                                      400: 'Bad Request',
                                      409: "Integrity Error",
                                      404: "Not Found",
                                      500: "Internal Server Error"})
    def delete(self, id):
        try:
            admin_route(request)
        except:
            return make_response(jsonify({"data": "Usuário não autorizado"}), 401)
        response = flask_adapter(request=request, composer=delete_product_composer(), arg=id)
        return make_response(jsonify(response), int(response["status"]))
