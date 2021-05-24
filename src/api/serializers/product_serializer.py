from flask_restplus import fields
from src.config.restplus import api


product_request = api.model('Product Request', {
    'name': fields.String(required=True, description='product name'),
    'code': fields.String(required=True, description='product code'),
    'cost_price': fields.Float(required=True, description='product cost_price'),
    'sell_price': fields.Float(required=True, description='product sell_price'),
    'stock': fields.Integer(required=True, description='product stock')
})

product_result = api.model('Product Result', {
    'id': fields.Integer(required=True, description='Product Id'),
    'name': fields.String(required=True, description='product name'),
    'code': fields.String(required=True, description='product code'),
    'cost_price': fields.Float(required=True, description='product cost_price'),
    'sell_price': fields.Float(required=True, description='product sell_price'),
    'stock': fields.Integer(required=True, description='product stock')
})
