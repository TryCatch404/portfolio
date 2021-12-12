from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
import geopy.distance
import requests
import urllib.parse

views = Blueprint('views', __name__)

@views.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    pass


@views.route('/', methods=['GET', 'POST'])
def home():
    """
        :function: home()
        :description: To render home templates.
        :parameters: None
        :return: Template with current logged in user
    """
    return render_template("index.html", user=current_user)

