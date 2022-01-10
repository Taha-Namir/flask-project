from flask import Blueprint, render_template

views = Blueprint('views', __name__) #defines a Blueprint for our website

@views.route('/')
def home():
    return render_template("index.html")