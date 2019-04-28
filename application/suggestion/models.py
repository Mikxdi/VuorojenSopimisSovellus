from application import db

class Suggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
 

    name = db.Column(db.String(144), nullable=False)
    when = db.Column(db.Date, nullable=False)
    location_id= db.Column(db.Integer, db.ForeignKey('location.id'), nullable = False)
    success = db.Column(db.Boolean, nullable = False)

    vote = db.relationship("Vote", backref = 'suggestion', cascade = "all, delete-orphan")

    def __init__(self, name, when, location_id, success):
        self.name = name
        self.when = when
        self.location_id = location_id
        self.success = success

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suggestion_id = db.Column(db.Integer, db.ForeignKey('suggestion.id'))
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __init__(self, suggestion_id, user_id):
        self.suggestion_id = suggestion_id
        self.user_id = user_id