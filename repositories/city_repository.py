from db.run_sql import run_sql
from models.city import City
from models.attraction import Attraction

import repositories.country_repository as country_repository


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def save(city):
    sql = "INSERT INTO cities (name, country_id, visited) VALUES (%s, %s, %s) RETURNING id"
    values = [city.name, city.country.id, city.visited]
    results = run_sql(sql, values)
    city.id = results[0]["id"]
    return city


def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row["country_id"])
        city = City(row["name"], country, row["visited"], row["id"])
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = country_repository.select(result["country_id"])
        city = City(result["name"], country, result["visited"], result["id"])
    return city


def update(city):
    sql = "UPDATE cities SET (name, country_id, visited) = (%s, %s, %s) WHERE id = %s"
    values = [city.name, city.country.id, city.visited, city.id]
    run_sql(sql, values)


def find_attraction_in_city(city):
    city_attractions = []
    sql = "SELECT * FROM attractions WHERE city_id = %s"
    values = [city.id]
    result = run_sql(sql, values)

    for row in result:
        attraction = Attraction(
            row["name"],
            row["description"],
            city,
            row["date"],
            row["visited"],
            row["id"],
        )
        city_attractions.append(attraction)
    return city_attractions


def find_city_by_name(city):
    searched_city = []
    sql = "SELECT * FROM cities WHERE name = %s"
    values = [city]
    results = run_sql(sql, values)
    for row in results:
        country = country_repository.select(row["country_id"])
        city = City(row["name"], country, row["visited"], row["id"])
        searched_city.append(city)
    return searched_city
