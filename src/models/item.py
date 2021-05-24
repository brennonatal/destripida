from . import db
from .product import Product  

#configura modelo de dados do ITEM
class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True) 
    quantity = db.Column(db.Integer())
    product_code = db.Column(db.String(255))
    product_id = db.Column(
        db.Integer, db.ForeignKey('product.id', ondelete='CASCADE'))
    product = db.relationship('Product')

    def __str__(self):
        return self.quantity

    def get_item_id(self):
        return self.id