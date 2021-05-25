from . import db

# configura modelo de dados do CLIENT


class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    cpf = db.Column(db.String(255))
    cellphone = db.Column(db.String(255))
    

    def __str__(self):
        return self.first_name, self.last_name

    def get_client_id(self):
        return self.id