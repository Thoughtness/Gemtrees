from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/trees')
def trees():
    return render_template("trees.html")

@auth.route('/order')
def order():
    return render_template("order.html")

@auth.route('/how-to')
def how_to():
    return render_template("how_to.html")

@auth.route('/about-me')
def about_me():
    return render_template("about_me.html")

