
from flask import Blueprint, render_template
# from flask_wtf import FlaskForm


hcode = Blueprint("hcode", __name__)


@hcode.route('/',methods=['GET', "POST"])
def home():
    return render_template("home.html")

