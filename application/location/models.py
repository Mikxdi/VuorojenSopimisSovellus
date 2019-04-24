from application import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
 

    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    suggestion = db.relationship("Suggestion", backref ='location', lazy = True)

    def __init__(self, name, when):
        self.name = name
        self.price = when
