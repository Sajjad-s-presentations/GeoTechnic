from app import db

class Tariff_list(db.Model):

    __tablename__ = 'tariff_list'

    id = db.Column(db.Integer, primary_key=True)
    id_no = db.Column(db.Integer, unique=True)
    description = db.Column(db.String(1000))

    def __repr__(self):
        return f'Tariff {self.id_no} is {self.description}'