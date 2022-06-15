from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
from models.attraction import Attraction
from models.countries_list import all_countries_list as list_of_all_countries
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.attraction_repository as attraction_repository

attractions_blueprint = Blueprint("attraction", __name__)

# Goes to attractions homepage listing all the attractions in the database
@attractions_blueprint.route("/attractions")
def attractions():
    if request.args:
        searched_attraction = request.args["attraction-searched"]
        attractions = attraction_repository.find_attraction_by_name(searched_attraction)
    else:
        attractions = attraction_repository.select_all()
    cities = city_repository.select_all()
    return render_template(
        "attractions/index.html", all_cities=cities, all_attractions=attractions
    )


# Goes to the attraction's page to list info
@attractions_blueprint.route("/attractions/<id>")
def show(id):
    attraction = attraction_repository.select(id)
    return render_template("attractions/show.html", attraction=attraction)


# Goes to page to add new attraction
@attractions_blueprint.route("/attractions/new", methods=["GET"])
def new_attraction():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    attractions = attraction_repository.select_all()
    return render_template(
        "attractions/new.html",
        cities=cities,
        countries=countries,
        attractions=attractions,
        list_of_countries=list_of_all_countries,
    )


# Adds new attraction to the list
@attractions_blueprint.route("/attractions", methods=["POST"])
def create_attraction():
    name = request.form["name"]
    description = request.form["description"]
    city_id = request.form["city_id"]
    city = city_repository.select(city_id)
    date = None
    visited = False
    attraction = Attraction(name, description, city, date, visited)
    attraction_repository.save(attraction)
    return redirect("/attractions")
