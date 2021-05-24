from flask_restplus import fields
from src.config.restplus import api


item_request = api.model('Item Request', {
    'quantity': fields.Integer(required=True, description='item quantity'),
    'product_code': fields.String(required=True, description='product code')
})

item_result = api.model('Item Result', {
    'id': fields.Integer(required=True, description='item Id'),
    'quantity': fields.Integer(required=True, description='item quantity'),
    'product_code': fields.String(required=True, description='product code'),
    'product_id': fields.Integer(required=True, description='item product ID'),
})
