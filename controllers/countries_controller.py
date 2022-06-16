from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.countries_list import all_countries_list as list_of_all_countries
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("country", __name__)


@countries_blueprint.route("/countries")
def countries():
    if request.args:
        searched_country = request.args["country-searched"]
        countries = country_repository.find_country_by_name(searched_country)
    else:
        countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries=countries)


@countries_blueprint.route("/countries/<id>")
def show(id):
    country = country_repository.select(id)
    city_in_country = country_repository.find_city_in_country(country)
    return render_template(
        "countries/show.html", country=country, city_in_country=city_in_country
    )


@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = country_repository.select(id)
    countries = country_repository.select_all()
    return render_template(
        "/countries/edit.html", country=country, all_countries=countries
    )


@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form["name"]
    region = request.form["region"]
    visited = False
    code = country_repository.select(id).code
    capital = request.form["capital"]
    country_update = Country(name, region, code, capital, visited, id)
    country_repository.update(country_update)
    return redirect("/countries")


@countries_blueprint.route("/countries/<id>/visited", methods=["POST"])
def update_country_as_visited(id):
    country = country_repository.select(id)
    country.set_visited()
    country_repository.update(country)
    return redirect("/countries")


@countries_blueprint.route("/countries/new", methods=["GET"])
def new_country():
    countries = country_repository.select_all()
    return render_template(
        "countries/new.html",
        countries=countries,
        list_of_countries=list_of_all_countries,
    )


@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    country = request.form["country"]
    new_country = Country(country, None, None, None)
    new_country_region = new_country.get_country_by_name(country)["continent"]
    new_country_code = new_country.get_country_by_name(country)["code"]
    new_country_capital = new_country.get_country_by_name(country)["capital"]
    new_country = Country(
        country, new_country_region, new_country_code, new_country_capital
    )
    country_repository.save(new_country)
    return redirect("/countries")


@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")


@countries_blueprint.route("/countries/travelled")
def visited_countries():
    countries = country_repository.select_all()
    return render_template("countries/travelled.html", countries=countries)


@countries_blueprint.route("/countries/not_travelled")
def unvisited_countries():
    countries = country_repository.select_all()
    return render_template("countries/not_travelled.html", countries=countries)
