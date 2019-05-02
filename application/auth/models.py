from application import db

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    roles = db.Column(db.String(144), nullable = False)

    vote = db.relationship("Vote", backref = 'account', cascade = "all, delete-orphan")
    suggestion = db.relationship("Suggestion", backref ='account', lazy = True)
    location = db.relationship("Location", backref ='account', lazy = True)

    def __init__(self, name, username, password, roles):
        self.name = name
        self.username = username
        self.password = password
        self.roles = roles
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

