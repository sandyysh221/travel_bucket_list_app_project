from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("country", __name__)

# Goes to Countries homepage listing all the countries in the database
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries=countries)


# Goes to the country's page to list info // code broke
@countries_blueprint.route("/countries/<id>")
def show(id):
    country = country_repository.select(id)
    city_in_country = country_repository.find_city_in_country(country)
    return render_template(
        "countries/show.html", country=country, city_in_country=city_in_country
    )


# @countries_blueprint.route("/countries/<id>/edit")
# def edit_country(id):
#     country = country_repository.select(id)
#     countries = country_repository.select_all()
#     return render_template(
#         "/countries/edit.html", country=country, all_countries=countries
#     )


# @countries_blueprint.route("/countries/<id>", methods=["POST"])
# def update_country(id):
#     country_id = request.form["country_id"]
#     name = country_repository.select(country_id)
#     region = request.form["region"]
#     country = Country(name, region, id)
#     country_repository.update(country)
#     return redirect("/countries")


# @countries_blueprint.route("/countries/new", methods=["GET"])
# def new_country():
#     countries = country_repository.select_all()
#     return render_template("countries/new.html", countries=countries)


# @countries_blueprint.route("/countries", methods=["POST"])
# def create_country():
#     name = request.form["name"]
#     new_country = Country(name, None, None)
#     new_country.region = new_country.get_country_by_name(country)["continent"]
#     new_country.code = new_country.get_country_by_name(country)["code"]
#     country_repository.save(new_country)
#     return redirect("/countries")
