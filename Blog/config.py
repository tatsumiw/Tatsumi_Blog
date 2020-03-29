#encoding: utf-8
#一些参数设置
import os

DEBUG = True #app.run()的参数设置

SECRET_KEY = os.urandom(24)

#数据库的相关参数设置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'blog'  #数据库名
USERNAME = 'root'
PASSWORD = 'abcdos940'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

USERNAME_LOGIN = 'Tatsumi'
PASSWORD_LOGIN = 'wenmao940'

SQLALCHEMY_TRACK_MODIFICATIONS = False