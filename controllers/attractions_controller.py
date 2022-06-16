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


@attractions_blueprint.route("/attractions/<id>")
def show(id):
    attraction = attraction_repository.select(id)
    return render_template("attractions/show.html", attraction=attraction)


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


@attractions_blueprint.route("/attractions/<id>", methods=["POST"])
def update_attraction(id):
    attraction = attraction_repository.select(id)
    attraction.set_visited()
    attraction_repository.update(attraction)
    return redirect("/attractions")


@attractions_blueprint.route("/attractions/travelled")
def visited_attractions():
    attractions = attraction_repository.select_all()
    return render_template("attractions/travelled.html", attractions=attractions)


@attractions_blueprint.route("/attractions/not_travelled")
def unvisited_attractions():
    attractions = attraction_repository.select_all()
    return render_template("attractions/not_travelled.html", attractions=attractions)


@attractions_blueprint.route("/attractions/<id>/delete", methods=["POST"])
def delete_attraction(id):
    attraction_repository.delete(id)
    return redirect("/attractions")
