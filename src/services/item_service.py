from src.models import db
from src.models.item import Item
from src.config.restplus import json_abort
from sqlalchemy.exc import SQLAlchemyError
import datetime

# importa a consulta de product e inclui um apelido ao get para evitar conflito com o get do item
from src.services.product_service import get as get_product

# ITEM SERVICE
# gerenciar as regras de negocio e CRUD do Item
###


def create(data):
    try:

        quantity = data.get('quantity')
        if not quantity:
            json_abort(400, "quantity is required")

        product_code = data.get('product_code')
        if not product_code:
            json_abort(400, "product code is required")

        product = get_product(product_code)

        if quantity > product.stock:
            json_abort(400, f'only {product.stock} {product.name} in stock')

        product.stock -= quantity

        product_id = product.id
        if not product_id:
            json_abort(400, "product id is required")

        item = Item(quantity=quantity,
                    product_code=product_code,
                    product_id=product_id,
                    product=product)

        db.session.add(item)
        db.session.commit()

        return item

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        item = Item.query.filter_by(id=id).first()

        if not item:
            json_abort(400, "item not found")
        else:
            return item

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def change(id, data):
    try:

        item = Item.query.filter_by(id=id).first()

        if not item:
            json_abort(400, "item not found")

        quantity = data.get('quantity')
        if not quantity:
            json_abort(400, "quantity is required")

        product_code = data.get('product_code')
        if not product_code:
            json_abort(400, "product code is required")

        product = get_product(product_code)

        product_id = product.id
        if not product_id:
            json_abort(400, "product id is required")

        # we must update the product stock if the quantity has changed
        diff_qtd = quantity - item.quantity
        
        # if the quantity has increased
        if diff_qtd > 0:
            # we gotta check the stock
            if diff_qtd > product.stock:
                json_abort(400, f'only {product.stock} {product.name} in stock')
            
            product.stock -= diff_qtd
        # if the quantity has decreased we add it back to the stock
        else:
            product.stock += abs(diff_qtd)

        item.quantity = quantity
        item.product_code = product_code
        item.product_id = product_id
        item.product = product

        db.session.commit()

        return item

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:

        item = Item.query.filter_by(id=id).first()

        if not item:
            json_abort(400, "item not found")
        else:
            product = get_product(item.product_code)
            product.stock += item.quantity

            db.session.delete(item)
            db.session.commit()

            return item

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)
