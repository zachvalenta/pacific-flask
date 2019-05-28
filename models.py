from pacific import db

class Input(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_first = db.Column(db.String(80), nullable=False)
    name_last = db.Column(db.String(80), nullable=False)
