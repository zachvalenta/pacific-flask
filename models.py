from pacific import db

class Input(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_first = db.Column(db.String(80))
    name_last = db.Column(db.String(80))
    address = db.Column(db.String(80))
    state = db.Column(db.String(80))
    zip = db.Column(db.Integer)
    status = db.Column(db.String(80))
    product_id = db.Column(db.Integer)
    product_name = db.Column(db.String(100))
    product_amount = db.Column(db.Numeric)
