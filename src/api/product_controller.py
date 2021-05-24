from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.product_serializer import product_request, product_result
from src.services.product_service import create, change, delete, get


ns = api.namespace('api/product', description='Operations related to product')


@ns.route('')  # define rota
class ProductCollection(Resource):
    # define parametro de entrada para a documentaçao do swagger
    @api.expect(product_request)
    @api.marshal_with(product_result)  # define resultado da metodo
    def post(self):
        """
        Create a new product
        """
        product = create(request.json)
        return product


@ns.route('/<string:code>')
class ProductIDCollection(Resource):
    @api.marshal_with(product_result)
    def get(self, code):
        """
        Get product by code
        """
        product = get(code)
        return product

    @api.expect(product_request)
    @api.marshal_with(product_result)
    def put(self, code):
        """
        Change product by code
        """
        product = change(code, request.json)
        return product

    @api.marshal_with(product_result)
    def delete(self, code):
        """
        Delete product by code
        """
        product = delete(code)
        return product
