from application import db
from sqlalchemy.sql import text

class Suggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
 

    name = db.Column(db.String(144), nullable=False)
    whenis = db.Column(db.Date, nullable=False)
    location_id= db.Column(db.Integer, db.ForeignKey('location.id'), nullable = False)
    success = db.Column(db.Boolean, nullable = False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    vote = db.relationship("Vote", backref = 'suggestion', cascade = "all, delete-orphan")

    def __init__(self, name, whenis, location_id, success, account_id):
        self.name = name
        self.whenis = whenis
        self.location_id = location_id
        self.success = success
        self.account_id = account_id
    
    @staticmethod
    def suggestionAndLocationListing():
        stmt = text("SELECT Suggestion.name, Suggestion.whenis, Location.name, Location.price, Suggestion.success, Suggestion.id, Account.id, COUNT(Vote.id) AS Votes FROM Suggestion"
        " JOIN Location ON Location.id = Suggestion.location_id" 
        " JOIN Account ON Account.id = Suggestion.account_id"
        " LEFT JOIN Vote ON Vote.suggestion_id = Suggestion.id"
        " GROUP BY Suggestion.name, Location.name, Suggestion.success, Suggestion.whenis, Location.price")
        
        res = db.engine.execute(stmt)

        resp = []
        for row in res:
            resp.append({"suggname":row[0], "when":row[1], "locname":row[2], "price":row[3], "success":row[4], "suggid":row[5], "account":row[6], "votes":row[7]})
        return resp


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suggestion_id = db.Column(db.Integer, db.ForeignKey('suggestion.id'))
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __init__(self, suggestion_id, account_id):
        self.suggestion_id = suggestion_id
        self.account_id = account_id