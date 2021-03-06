from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "SECRET KEY"

connect_db(app)


@app.route("/")
def home_page():
    """display home page with list of pets"""

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)


@app.route("/add/", methods=["GET", "POST"])
def add_pet():
    """displays form to add a pet, and handles submitting new pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        new_pet = Pet(
            name=name,
            species=species,
            age=age,
            photo_url=photo_url,
            notes=notes,
            available=available,
        )
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added {name} to pets", "success")
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)


@app.route("/<pet_id>/", methods=["GET", "POST"])
def pet_info(pet_id):
    """displays information about a specific pet"""

    pet = Pet.query.get(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} updated!", "success")
        return render_template("pet_details.html", pet=pet, form=form)
    else:
        return render_template("pet_details.html", pet=pet, form=form)


@app.route("/<pet_id>/delete/", methods=["POST"])
def delete_pet(pet_id):
    """removes given pet from db"""

    pet = Pet.query.get(pet_id)
    db.session.delete(pet)
    db.session.commit()

    flash(f"{pet.name} has been deleted", "danger")
    return redirect("/")