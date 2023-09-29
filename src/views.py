from flask import Blueprint, render_template
import sys

#from checksheet_reader.checksheet_to_node import nodeCreation

#sys.path.insert(1, "C://Users//Connor//Documents//GitHub//What-If")
#import Comparison


views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/settings")
def settings():
    return render_template("settings.html")


@views.route("/review")
def review():
    return render_template("website/templates/review.html")


@views.route("/about")
def about():
    return render_template("about.html")


@views.route("/final")
def final():
    #good_credits = Comparison.good
    #bad_credits = Comparison.bad
    return render_template("final.html", good_credits='', bad_credits='bad_credits')
