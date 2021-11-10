from flask_restx import Resource, Namespace
from flask import request, jsonify, make_response
from src.domain.dto import Product as ProductDto
from src.main.adapters import flask_adapter
from src.domain.dto import ProductToUpdate as ProductToUpdateDto
from src.domain.dto import ProductRemoveAmount as RemoveAmountDto
from src.main.utils import admin_route
from src.main.compose import create_product_composer
from src.main.compose import list_products_composer
from src.main.compose import remove_amount_composer
from src.main.compose import upload_image_composer
from src.main.compose.product.delete_product_composer import delete_product_composer
from src.main.compose.product.update_product_composer import update_product_composer
from src.main.compose import get_image_composer
from werkzeug.datastructures import FileStorage
from flask import current_app as app
import os
import base64

product_namespace = Namespace('products')
product = product_namespace.model('Product', ProductDto)
remove_amount = product_namespace.model('RemoveAmount', RemoveAmountDto)
product_update = product_namespace.model('ProductToUpdate', ProductToUpdateDto)
parser = product_namespace.parser()
parser.add_argument('Authorization', location='headers')

upload_parser = product_namespace.parser()
upload_parser.add_argument('files', location='files',
                           type=FileStorage, required=True)
upload_parser.add_argument('Authorization', location='headers')

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

    @product_namespace.expect(remove_amount)
    @product_namespace.doc(responses={200: 'OK',
                                      400: 'Bad Request',
                                      409: "Integrity Error",
                                      404: "Not Found",
                                      500: "Internal Server Error"})
    def patch(self):
        response = flask_adapter(request, remove_amount_composer())
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

@product_namespace.route('/img/<int:id>', endpoint='product-images')
@product_namespace.doc(params={"id": "Id do produto"})
@product_namespace.expect(upload_parser)
class ProductActions(Resource):
    @product_namespace.doc(responses={200: 'OK',
                                      400: 'Bad Request',
                                      409: "Integrity Error",
                                      404: "Not Found",
                                      500: "Internal Server Error"})
    def post(self, id):
        try:
            admin_route(request)
        except:
            return make_response(jsonify({"data": "Usuário não autorizado"}), 401)
        response = flask_adapter(request=request, composer=upload_image_composer(), arg=id)
        return make_response(jsonify(response), int(response["status"]))
