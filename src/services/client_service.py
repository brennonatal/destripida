from src.models import db
from src.models.client import Client
from src.config.restplus import json_abort
from sqlalchemy.exc import SQLAlchemyError

# CLIENT SERVICE
# gerenciar as regras de negocio e CRUD do client
###


def create(data):
    try:

        first_name = data.get('first_name')
        if not first_name:
            json_abort(400, "First name is required")

        last_name = data.get('last_name')
        if not last_name:
            json_abort(400, "Last name is required")

        email = data.get('email')
        if not email:
            json_abort(400, "E-mail is required")

        cpf = data.get('cpf')
        if not cpf:
            json_abort(400, "CPF is required")

        cellphone = data.get('cellphone')
        if not cellphone:
            json_abort(400, "Cellphone is required")

        client = Client(first_name=first_name,
                        last_name=last_name,
                        email=email,
                        cpf=cpf,
                        cellphone=cellphone)

        db.session.add(client)
        db.session.commit()

        return client

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:

        client = Client.query.filter_by(id=id).first()

        if not client:
            json_abort(400, "Client not found")
        else:
            return client

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def change(id, data):
    try:

        client = Client.query.filter_by(id=id).first()

        if not client:
            json_abort(400, "Product not found")
        else:

            first_name = data.get('first_name')
            if not first_name:
                json_abort(400, "First name is required")

            last_name = data.get('last_name')
            if not last_name:
                json_abort(400, "Last name is required")

            email = data.get('email')
            if not email:
                json_abort(400, "E-mail is required")

            cpf = data.get('cpf')
            if not cpf:
                json_abort(400, "CPF is required")

            cellphone = data.get('cellphone')
            if not cellphone:
                json_abort(400, "Cellphone is required")

            client.first_name = first_name
            client.last_name = last_name
            client.email = email
            client.cpf = cpf
            client.cellphone = cellphone

            db.session.commit()

            return client

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:

        client = Client.query.filter_by(id=id).first()

        if not client:
            json_abort(400, "Client not found")
        else:
            db.session.delete(client)
            db.session.commit()

            return client

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)
