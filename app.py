from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)


@app.route("/")
def home_page():
    """display home page with list of pets"""

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)
