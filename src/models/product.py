from . import db

# configura modelo de dados do PRODUCT


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    code = db.Column(db.String(255), unique=True)
    cost_price = db.Column(db.Float())
    sell_price = db.Column(db.Float())
    stock = db.Column(db.Integer())

    def __str__(self):
        return self.name

    def get_product_id(self):
        return self.id
