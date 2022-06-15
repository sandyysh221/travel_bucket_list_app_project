from db.run_sql import run_sql
from models.country import Country
from models.city import City


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def save(country):
    sql = "INSERT INTO countries(name, code, region, capital, visited) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [
        country.name,
        country.code,
        country.region,
        country.capital,
        country.visited,
    ]
    results = run_sql(sql, values)
    country.id = results[0]["id"]
    return country


def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        country = Country(
            row["name"],
            row["region"],
            row["code"],
            row["capital"],
            row["visited"],
            row["id"],
        )
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(
            result["name"],
            result["region"],
            result["code"],
            result["capital"],
            result["visited"],
            result["id"],
        )
    return country


def update(country):
    sql = "UPDATE countries SET (name, region, code, capital, visited) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [
        country.name,
        country.region,
        country.code,
        country.capital,
        country.visited,
        country.id,
    ]
    run_sql(sql, values)


def find_city_in_country(country):
    country_cities = []
    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    result = run_sql(sql, values)

    for row in result:
        city = City(row["name"], country, row["id"])
        country_cities.append(city)
    return country_cities


def find_country_by_name(country):
    searched_country = []
    sql = "SELECT * FROM countries WHERE name = %s"
    values = [country]
    results = run_sql(sql, values)
    for row in results:
        country = Country(
            row["name"],
            row["region"],
            row["code"],
            row["capital"],
            row["visited"],
            row["id"],
        )
        searched_country.append(country)
    return searched_country
