from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
from models.countries_list import all_countries_list as list_of_all_countries
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

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
        "cities/new.html", cities=cities, list_of_countries=list_of_all_countries
    )


# Adds new city to the list
@cities_blueprint.route("/cities", methods=["POST"])
def create_city():
    name = request.form["name"]
    country = request.form["country"]
    new_country = Country(country, None, None)
    new_country_region = new_country.get_country_by_name(country)["continent"]
    new_country_code = new_country.get_country_by_name(country)["code"]
    new_country = Country(country, new_country_region, new_country_code)
    new_country = country_repository.save(new_country)
    visited = request.form["visited"]
    city = City(name, new_country, visited)
    city_repository.save(city)
    return redirect("/cities")
