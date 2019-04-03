from application import db

class Suggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
 

    name = db.Column(db.String(144), nullable=False)
    when = db.Column(db.Date, nullable=False)

    def __init__(self, name, when):
        self.name = name
        self.when = when
