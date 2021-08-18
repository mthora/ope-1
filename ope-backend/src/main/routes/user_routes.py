from flask_restx import Resource, Namespace
from flask import request, jsonify, make_response
from src.domain.dto import User as UserDto
from src.main.adapters import flask_adapter

from src.main.compose import create_user_composer

user_namespace = Namespace('users')
user = user_namespace.model('User', UserDto)

users = []


@user_namespace.route('/')
class ListUsers(Resource):

    @user_namespace.marshal_list_with(user, code=200)
    def get(self):
        return users

    @user_namespace.expect(user)
    def post(self):
        response = flask_adapter(request, create_user_composer())
        return make_response(jsonify(response), int(response["status"]))
