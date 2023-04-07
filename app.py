from flask import Flask,jsonify,request

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS,cross_origin

db = SQLAlchemy()


app=Flask(__name__)



Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'



# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

import datetime



class Articles(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    body=db.Column(db.Text())
    date=db.Column(db.DateTime,default=datetime.datetime.now)

    def __init__(self,title,body):
        self.title=title
        self.body=body


ma=Marshmallow(app)

class ArticleSchema(ma.Schema):
    class Meta:
        fields=('id','title','body','date')


article_schema=ArticleSchema()
articles_schema=ArticleSchema(many=True)


@app.route("/get_all_articles",methods=['GET'])
def get_articles():
    all_query_Art=Articles.query.all()
    results=articles_schema.dump(all_query_Art)
    return jsonify(results)


@app.route("/get_article/<id>",methods=['GET'])
def get_article_id(id):
    query_art=Articles.query.get(id)
    result=article_schema.jsonify(query_art)
    return result


@app.route("/add_article",methods=["POST"])
def add_article():
    title=request.json['title']
    body=request.json['body']

    articles_obj = Articles(title,body)
    db.session.add(articles_obj)
    db.session.commit()
    return article_schema.jsonify(articles_obj)


@app.route("/update_article/<id>",methods=["PUT"])
def update_article(id):
    query_art=Articles.query.get(id)
    title=request.json['title']
    body=request.json['body']

    query_art.title=title
    query_art.body=body
    db.session.commit()
    return article_schema.jsonify(query_art)

@app.route("/delete_article/<id>",methods=["DELETE"])
def delete_article(id):
    query_art=Articles.query.get(id)
    db.session.delete(query_art)
    db.session.commit()
    return article_schema.jsonify(query_art)




if __name__=="__main__":
    app.run(debug=True)

