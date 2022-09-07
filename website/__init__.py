from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db=SQLAlchemy()
#DB_NAME="database.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='kjbncbvoiwhjapoj jng'


   #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://oookzitxsuscwt:59ec8d019bb0f67f5e1e79200507345ea88a77f7d5f2d181660dd51acc19b8f9@ec2-3-234-131-8.compute-1.amazonaws.com:5432/dciqmthf0s9chv'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User, Book
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    # if not path.exists('website/' + DB_NAME):
    db.create_all(app=app)
        # print('Created Database!')

