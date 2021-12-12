from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth
from flask_migrate import Migrate


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='FitnessApp', template_mode='bootstrap3')

    app.config['BASIC_AUTH_USERNAME'] = 'admin'
    app.config['BASIC_AUTH_PASSWORD'] = 'admin'

    basic_auth = BasicAuth(app)

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    admin.add_view(ModelView(User, db.session))

    create_database(app)

    return app


def create_database(app):
    db.create_all(app=app)
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

