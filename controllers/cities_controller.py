from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
from models.countries_list import all_countries_list as list_of_all_countries
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("city", __name__)


@cities_blueprint.route("/cities")
def cities():
    if request.args:
        searched_city = request.args["city-searched"]
        cities = city_repository.find_city_by_name(searched_city)
    else:
        cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template(
        "cities/index.html", all_cities=cities, all_countries=countries
    )


@cities_blueprint.route("/cities/new", methods=["GET"])
def new_city():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template(
        "cities/new.html",
        cities=cities,
        countries=countries,
        list_of_countries=list_of_all_countries,
    )


@cities_blueprint.route("/cities", methods=["POST"])
def create_city():
    name = request.form["name"]
    country_id = request.form["country_id"]
    country = country_repository.select(country_id)
    visited = False
    city = City(name, country, visited)
    city_repository.save(city)
    return redirect("/cities")


@cities_blueprint.route("/cities/<id>")
def show(id):
    city = city_repository.select(id)
    attractions_in_city = city_repository.find_attraction_in_city(city)
    return render_template(
        "cities/show.html", city=city, attractions_in_city=attractions_in_city
    )


@cities_blueprint.route("/cities/<id>/edit")
def edit_city(id):
    city = city_repository.select(id)
    cities = city_repository.select_all()
    return render_template("/cities/edit.html", city=city, all_cities=cities)


@cities_blueprint.route("/cities/<id>", methods=["POST"])
def update_city(id):
    city = city_repository.select(id)
    city.set_visited()
    city_repository.update(city)
    return redirect("/cities")


@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/cities")


@cities_blueprint.route("/cities/travelled")
def visited_cities():
    cities = city_repository.select_all()
    return render_template("cities/travelled.html", cities=cities)


@cities_blueprint.route("/cities/not_travelled")
def unvisited_cities():
    cities = city_repository.select_all()
    return render_template("cities/not_travelled.html", cities=cities)
