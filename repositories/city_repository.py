from db.run_sql import run_sql
from models.city import City

import repositories.country_repository as country_repository


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def save(city):
    sql = "INSERT INTO cities (name, country_id) VALUES (%s, %s) RETURNING id"
    values = [city.name, city.country.id]
    results = run_sql(sql, values)
    city.id = results[0]["id"]
    return city


def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row["country_id"])
        city = City(row["name"], country, row["id"])
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = country_repository.select(result["country_id"])
        city = City(result["name"], country, result["id"])
    return city


def update(city):
    pass
