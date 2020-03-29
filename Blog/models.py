#encoding: utf-8
#保存数据库模型

from exts import db #导入db对象
from datetime import datetime

class Dynamic(db.Model):
    __tablename__ = 'dynamic'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    label = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(1024),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)
    read_times = db.Column(db.Integer,nullable=False)

class Commenary(db.Model):
    __tablename__ = 'commenary'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    article_id = db.Column(db.Integer,db.ForeignKey('article.id'))

    article = db.relationship('Article', backref=db.backref('commenarys',order_by = create_time.desc()))

