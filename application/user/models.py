from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
 

    name = db.Column(db.String(144), nullable=False)
    nick = db.Column(db.String(144), nullable=False)

    def __init__(self, name, nick):
        self.name = name
        self.nick =nick

