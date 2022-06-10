from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("country", __name__)
