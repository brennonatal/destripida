from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.client_serializer import client_request, client_result
from src.services.client_service import create, change, delete, get


ns = api.namespace('api/client', description='Operations related to client')


@ns.route('')  # define rota
class ClientCollection(Resource):
    # define parametro de entrada para a documentaçao do swagger
    @api.expect(client_request)
    @api.marshal_with(client_result)  # define resultado da metodo
    def post(self):
        """
        Create a new client
        """
        client = create(request.json)
        return client


@ns.route('/<int:id>')
class ClientIDCollection(Resource):
    @api.marshal_with(client_result)
    def get(self, id):
        """
        Get client by id
        """
        client = get(id)
        return client

    @api.expect(client_request)
    @api.marshal_with(client_result)
    def put(self, id):
        """
        Change client by id
        """
        client = change(id, request.json)
        return client

    @api.marshal_with(client_result)
    def delete(self, id):
        """
        Delete client by id
        """
        client = delete(id)
        return client
