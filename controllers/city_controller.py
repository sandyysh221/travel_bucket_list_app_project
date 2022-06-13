from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("city", __name__)

# Goes to Cities homepage listing all the cities in the database
@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities=cities)


# Goes to page to add new city
@cities_blueprint.route("/cities/new", methods=["GET"])
def new_city():
    cities = city_repository.select_all()
    return render_template(
        "cities/new.html",
        cities=cities,
    )


# Adds new city to the list
@cities_blueprint.route("/cities", methods=["POST"])
def create_city():
