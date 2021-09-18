from flask_restx import Resource, Namespace
from flask import request, jsonify, make_response
from src.domain.dto import User as UserDto
from src.domain.dto import LoginUser as LoginUserDto
from src.domain.dto import UserToUpdate as UserToUpdateDto
from src.main.adapters import flask_adapter
from src.main.utils import admin_route
from src.main.compose import create_user_composer
from src.main.compose import list_users_composer
from src.main.compose.user.get_user_by_id_composer import get_user_composer
from src.main.compose.user.update_user_composer import update_user_composer
from src.main.compose.user.delete_user_composer import delete_user_composer
from src.main.compose.user.login_user_composer import login_user_composer

user_namespace = Namespace('users')
user = user_namespace.model('User', UserDto)
login_user = user_namespace.model('LoginUser', LoginUserDto)
user_update = user_namespace.model('UserToUpdate', UserToUpdateDto)
parser = user_namespace.parser()
parser.add_argument('Authorization', location='headers')


@user_namespace.route('/')
@user_namespace.expect(parser)
class Users(Resource):

    @user_namespace.expect(user)
    @user_namespace.doc(responses={201: 'Created',
                                   401: 'Unauthorized',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   500: "Internal Server Error"})
    def post(self):
        try:
            admin_route(request)
        except:
            return make_response(jsonify({"data": "Usuário não autorizado"}), 401)
        response = flask_adapter(request, create_user_composer())
        return make_response(jsonify(response), int(response["status"]))

    @user_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   500: "Internal Server Error"})
    def get(self):
        try:
            admin_route(request)
        except:
            return make_response(jsonify({"data": "Usuário não autorizado"}), 401)
        response = flask_adapter(request, list_users_composer())
        return make_response(jsonify(response), int(response["status"]))

    @user_namespace.expect(user_update)
    @user_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   404: "Not Found",
                                   500: "Internal Server Error"})
    def put(self):
        try:
            admin_route(request)
        except:
            return make_response(jsonify({"data": "Usuário não autorizado"}), 401)
        response = flask_adapter(request, update_user_composer())
        return make_response(jsonify(response), int(response["status"]))


@user_namespace.route('/<int:id>', endpoint='users')
@user_namespace.expect(parser)
@user_namespace.doc(params={"id": 'Id do usuário'})
class UserActions(Resource):
    @user_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   404: "Not Found",
                                   500: "Internal Server Error"})
    def get(self, id):
        try:
            admin_route(request)
        except:
            return make_response(jsonify({"data": "Usuário não autorizado"}), 401)
        response = flask_adapter(request=request, composer=get_user_composer(), arg=id)
        return make_response(jsonify(response), int(response["status"]))

    @user_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   404: "Not Found",
                                   500: "Internal Server Error"})
    def delete(self, id):
        try:
            admin_route(request)
        except:
            return make_response(jsonify({"data": "Usuário não autorizado"}), 401)
        response = flask_adapter(request=request, composer=delete_user_composer(), arg=id)
        return make_response(jsonify(response), int(response["status"]))


@user_namespace.route('/login', endpoint='auth')
class UserLogin(Resource):
    @user_namespace.expect(login_user)
    @user_namespace.doc(responses={200: 'OK',
                                   400: "Bad Request",
                                   401: "Unauthorized",
                                   409: "Integrity Error",
                                   404: "Not Found",
                                   500: "Internal Server Error"})
    def post(self):
        response = flask_adapter(request, login_user_composer())
        return make_response(jsonify(response), int(response["status"]))