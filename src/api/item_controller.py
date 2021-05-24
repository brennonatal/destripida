from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.item_serializer import item_request, item_result
from src.services.item_service import create, change, delete, get


ns = api.namespace('api/item', description='Operations related to item')


@ns.route('')  # refine rota
class ItemCollection(Resource):
    # define parametro de entrada para a documentaçao do swagger
    @api.expect(item_request)
    @api.marshal_with(item_result)  # define resultado da metodo
    def post(self):
        """
        Create a new item
        """
        item = create(request.json)
        return item


@ns.route('/<int:id>')
class ItemIDCollection(Resource):
    @api.marshal_with(item_result)
    def get(self, id):
        """
        Get item by ID
        """
        item = get(id)
        return item

    @api.expect(item_request)
    @api.marshal_with(item_result)
    def put(self, id):
        """
        Change item by ID
        """
        item = change(id, request.json)
        return item

    @api.marshal_with(item_result)
    def delete(self, id):
        """
        Delete item by ID
        """
        item = delete(id)
        return item
