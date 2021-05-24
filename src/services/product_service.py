from src.models import db
from src.models.product import Product
from src.config.restplus import json_abort
from sqlalchemy.exc import SQLAlchemyError

# PRODUCT SERVICE
# gerenciar as regras de negocio e CRUD do product
###


def create(data):
    try:

        name = data.get('name')
        if not name:
            json_abort(400, "Product name is required")

        code = data.get('code')
        if not code:
            json_abort(400, "Product code is required")

        cost_price = data.get('cost_price')
        if not cost_price:
            json_abort(400, "Cost price is required")

        sell_price = data.get('sell_price')
        if not sell_price:
            json_abort(400, "Sell price is required")

        stock = data.get('stock')
        if not stock:
            json_abort(400, "Available stock is required")

        product = Product(name=name,
                          code=code,
                          cost_price=cost_price,
                          sell_price=sell_price,
                          stock=stock)

        db.session.add(product)
        db.session.commit()

        return product

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(code):
    try:

        product = Product.query.filter_by(code=code).first()

        if not product:
            json_abort(400, "Product not found")
        else:
            return product

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def change(code, data):
    try:

        product = Product.query.filter_by(code=code).first()

        if not product:
            json_abort(400, "Product not found")
        else:

            name = data.get('name')
            if not name:
                json_abort(400, "Product name is required")

            code = data.get('code')
            if not code:
                json_abort(400, "Product code is required")

            cost_price = data.get('cost_price')
            if not cost_price:
                json_abort(400, "Cost price is required")

            sell_price = data.get('sell_price')
            if not sell_price:
                json_abort(400, "Sell price is required")

            stock = data.get('stock')
            if not stock:
                json_abort(400, "Available stock is required")

            product.name = name
            product.code = code
            product.cost_price = cost_price
            product.cost_price = cost_price
            product.stock = stock

            db.session.commit()

            return product

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(code):
    try:

        product = Product.query.filter_by(code=code).first()

        if not product:
            json_abort(400, "product not found")
        else:
            db.session.delete(product)
            db.session.commit()

            return product

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)
