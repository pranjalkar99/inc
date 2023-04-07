from app import db
import datetime



class Articles(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    body=db.Column(db.Text())
    date=db.Column(db.DateTime,default=datetime.datetime.now)

    def __init__(self,title,body):
        self.title=title
        self.body=body

