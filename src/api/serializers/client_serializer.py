from flask_restplus import fields
from src.config.restplus import api


client_request = api.model('Client Request', {
    'first_name': fields.String(required=True, description='client first_name'),
    'last_name': fields.String(required=True, description='client last_name'),
    'email': fields.String(required=True, description='client email'),
    'cpf': fields.String(required=True, description='client cpf'),
    'cellphone': fields.String(required=True, description='client cellphone')
})

client_result = api.model('Client Result', {
    'id': fields.Integer(required=True, description='client Id'),
    'first_name': fields.String(required=True, description='client first_name'),
    'last_name': fields.String(required=True, description='client last_name'),
    'email': fields.String(required=True, description='client email'),
    'cpf': fields.String(required=True, description='client cpf'),
    'cellphone': fields.String(required=True, description='client cellphone')
})
