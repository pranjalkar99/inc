from flask import Flask,jsonify,request
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS,cross_origin
from datetime import datetime
# from sqlalchemy import Column, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity
from werkzeug.utils import secure_filename
db = SQLAlchemy()
from marshmallow import Schema, fields

app=Flask(__name__)

jwt = JWTManager(app)

app.config["JWT_SECRET_KEY"] = "this-is-secret-key-jwt" #change it
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'



# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

import datetime


import uuid

import arrow


@celery.task
def update_last_logged(user_id):
    user = User.query.get(user_id)
    if user:
        user.last_logged =arrow.utcnow().isoformat()
        user.fullname="Hagu Bora"
        db.session.commit()
def generate_handle_id(username):
    unique_chars = str(uuid.uuid4().hex)[:6]
    handle_id = username.replace(" ", "_").lower() + "_" + unique_chars
    return handle_id


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    image = db.Column(db.Text(),nullable=True)
    likes = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, body, author_id):
        self.title = title
        self.body = body
        self.likes = 0
        self.author_id = author_id



class Follower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, follower_id, followed_id):
        self.follower_id = follower_id
        self.followed_id = followed_id


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))
    image_link=db.Column(db.String(100))
    number=db.Column(db.String(10),nullable=True)
    bio = db.Column(db.String(100), nullable=True)
    # date_of_birth = db.Column(db.Date)
    date_of_birth = db.Column(db.String(10))
    last_logged = db.Column(db.String(50), default=arrow.utcnow().isoformat())
    handle_id = db.Column(db.String(50), unique=True)
    followers = db.relationship('Follower', foreign_keys='Follower.followed_id', backref='followed_by', lazy='dynamic')
    follows = db.relationship('Follower', foreign_keys='Follower.follower_id', backref='follows', lazy='dynamic')

    def __init__(self, fullname, username, password, date_of_birth, handle_id, image_link=None,number=None,bio=None):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.date_of_birth = date_of_birth
        self.handle_id = handle_id
        self.image_link = image_link
        self.bio=bio
        self.number=number

    def __repr__(self):
        return f"<User {self.username}>"
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
ma=Marshmallow(app)

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    fullname = fields.String(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class ArticleSchema(ma.Schema):
    class Meta:
        fields=('id','title','body','date','likes','author_id')


article_schema=ArticleSchema()
articles_schema=ArticleSchema(many=True)


@app.route("/test",methods=["POST"])
def test():
    name=request.form['name']
    print(name)
    return "Successful"

## Authentication
@app.route("/register", methods=["POST"])
def register():
    if request.is_json:
        username = request.json.get("username", None)
        
    else:
        username = request.form.get("username", None)
        
    # test = User.query.filter_by(email=email).first()
    test = User.query.filter_by(username=username).first()
    if test:
        return jsonify(message="User Already Exist"), 409
    else:
        if request.is_json:
            fullname = request.json.get("fullname", None)
            password = request.json.get("password", None)
            date_of_birth = request.json.get("date_of_birth", None)
        else:
            fullname = request.form.get("fullname", None)
            password = request.form.get("password", None)
            date_of_birth = request.form.get("date_of_birth", None)
        handle_id=generate_handle_id(fullname)
        

        user_info = User(fullname=fullname, username=username, password=generate_password_hash(password), date_of_birth=date_of_birth,handle_id=handle_id)
        db.session.add(user_info)
        db.session.commit()
        access_token = create_access_token(identity=user_info.id)
        return jsonify({"access_token": access_token}), 200


@app.route("/get_profile")
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    else:
        return jsonify({'username':user.username,'fullname':user.fullname,'handle':user.handle_id,'bio':user.bio,'dob':user.date_of_birth,'image':user.image_link,'number':user.number }),200
            
    
@app.route("/update-dp", methods=["POST","PUT"])  
@jwt_required()   
def update_photo():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    else:
        file=request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(f'uploads/{filename}')
            image_link = f"../../../uploads/{filename}" 
            user.image_link=image_link
            db.session.commit()
            return jsonify({'message': 'DP updated successfully...'}), 200


@app.route("/articles/<article_id>/like", methods=["POST","PUT"])  
@jwt_required() 
def like_Art(article_id):
    current_user_id = get_jwt_identity()
    user_e = User.query.filter_by(id=current_user_id).first()
    if not user_e:
        return jsonify({'message': 'User not found'}), 404
    else:
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form
        art=Articles.query.filter_by(id=article_id, author_id=user_e.id ).first()
        if data.get('likes'):
            art.likes+=1
            db.session.commit()

            return {"msg":"Updated the like"},201





@app.route("/update_profile", methods=["POST","PUT"])  
@jwt_required() 
def update_profile():
    current_user_id = get_jwt_identity()
    user_e = User.query.filter_by(id=current_user_id).first()
    if not user_e:
        return jsonify({'message': 'User not found'}), 404
    else:
        try:
            if request.is_json:
                data = request.get_json()
            else:
                data = request.form
            # Check if the fields are not empty before updating
            user_e.fullname = data.get('fullname', user_e.fullname) if data.get('fullname') else user_e.fullname
            user_e.image_link = data.get('image_link', user_e.image_link) if data.get('image_link') else user_e.image_link
            user_e.number = data.get('number', user_e.number) if data.get('number') else user_e.number
            user_e.bio = data.get('bio', user_e.bio) if data.get('bio') else user_e.bio
            user_e.date_of_birth = data.get('date_of_birth', user_e.date_of_birth) if data.get('date_of_birth') else user_e.date_of_birth
            db.session.commit()
            return jsonify("User uopdated Successfully.",201)

            fullname = request.form.get("fullname", None)
            # username = request.form.get("username", None)
            date_of_birth= request.form.get("username", None)
            number= request.form.get("number", None)
            bio=request.form.get("bio", None)
            # file=request.files['file']
            # file=request.files['file']
            user.fullname=fullname
            user.number=number
            user.bio=bio
            db.session.add(user)
            db.commit()
            return "DOne",201
        except Exception as e:
            return e
        
from datetime import datetime

@app.route("/login", methods=["POST"])
def login():
    if request.is_json:
        username = request.json.get("username", None)
        password = request.json.get("password", None)
    else:
        username = request.form.get("username", None)
        password = request.form.get("password", None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"msg": "Bad username or password"}), 401

    if not check_password_hash(user.password, password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=user.id)
    update_last_logged.delay(user.id)
    return jsonify(access_token=access_token), 200

@app.route("/dashboard")
@jwt_required
def dasboard():
    return jsonify(message="Welcome! to the Data Science Learner")

## nOrmal Routes

@app.route("/get_all_articles",methods=['GET'])
# # @jwt_required
# def get_articles_now():
#     final={}
#     # current_user_id = get_jwt_identity()
#     # user_o = User.query.filter_by(id=current_user_id).first()
#     # if not user_o:
#     # #     return jsonify({'message': 'Articles not found'}), 404
#     all_query_Art=Articles.query.all()
#     # for each_Article in all_query_Art:
#     #     obj=User.query.filter_by(id=each_Article.author_id)
        
#     #     final[each_Article.id]={each_Article, jsonify(obj)}
#     results=articles_schema.dump(all_query_Art)
#     return results
def get_all_articles():
    articles = Articles.query.join(User, Articles.author_id == User.id).with_entities(
        Articles.id, Articles.title, Articles.body, Articles.date, Articles.likes, User.fullname, User.handle_id
    ).all()

    article_list = []
    for article in articles:
        article_dict = {
            'id': article.id,
            'title': article.title,
            'body': article.body,
            'date': article.date,
            'likes': article.likes,
            'author_fullname': article.fullname,
            'author_handle':article.handle_id
        }
        article_list.append(article_dict)

    return jsonify(article_list)


@app.route("/get_article/<id>",methods=['GET'])
def get_article_id(id):
    query_art=Articles.query.get(id)
    result=article_schema.jsonify(query_art)
    return result

@app.route("/add_article",methods=["PUT"])
@jwt_required() 
def add_article():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    if request.is_json:
        title = request.json.get("title", None)
        body = request.json.get("body", None)
    else:
        title = request.form.get("title", None)
        body = request.form.get("body", None)

    articles_obj = Articles(title,body,author_id=user.id)

    db.session.add(articles_obj)
    db.session.commit()
    return jsonify({"msg": "Added to db "}), 201



@app.route("/update_article/<id>",methods=["PUT"])
@jwt_required() 
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
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=7000)

