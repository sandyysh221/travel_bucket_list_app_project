from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.countries_list import all_countries_list as list_of_all_countries
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("country", __name__)

# Goes to Countries homepage listing all the countries in the database
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries=countries)


# Goes to the country's page to list info
@countries_blueprint.route("/countries/<id>")
def show(id):
    country = country_repository.select(id)
    city_in_country = country_repository.find_city_in_country(country)
    return render_template(
        "countries/show.html", country=country, city_in_country=city_in_country
    )


# Goes to page to update country
@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = country_repository.select(id)
    countries = country_repository.select_all()
    return render_template(
        "/countries/edit.html", country=country, all_countries=countries
    )


# To update a country
@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form["name"]
    region = request.form["region"]
    visited = request.form["visited"]
    print(visited)
    code = country_repository.select(id).code
    country_update = Country(name, region, code, visited, id)
    country_repository.update(country_update)
    return redirect("/countries")


# Goes to page to add new country
@countries_blueprint.route("/countries/new", methods=["GET"])
def new_country():
    countries = country_repository.select_all()
    return render_template(
        "countries/new.html",
        countries=countries,
        list_of_countries=list_of_all_countries,
    )


# Adds new country to the list
@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    country = request.form["country"]
    new_country = Country(country, None, None)
    new_country_region = new_country.get_country_by_name(country)["continent"]
    new_country_code = new_country.get_country_by_name(country)["code"]
    new_country = Country(country, new_country_region, new_country_code)
    country_repository.save(new_country)
    return redirect("/countries")
