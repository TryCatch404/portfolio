from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy_utils import IntRangeType
import enum
# from website.auth import login
from flask import redirect, url_for, request
# from flask_admin.contrib import sqla

# class MicroBlogModelView(sqla.ModelView):
#
#     def is_accessible(self):
#         return login.current_user.is_authenticated
#
#     def inaccessible_callback(self, name, **kwargs):
#         # redirect to login page if user doesn't have access
#         return redirect(url_for('login', next=request.url))


class Gender(enum.Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
