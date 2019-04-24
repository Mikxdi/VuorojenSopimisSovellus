from application import db

class Suggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
 

    name = db.Column(db.String(144), nullable=False)
    when = db.Column(db.Date, nullable=False)
    location_id= db.Column(db.Integer, db.ForeignKey('location.id'), nullable = False)

    def __init__(self, name, when, location_id):
        self.name = name
        self.when = when
        self.location_id = location_id
