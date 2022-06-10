from db.run_sql import run_sql
from models.country import Country


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def save(country):
    sql = "INSERT INTO countries(name, region) VALUES (%s, %s) RETURNING id"
    values = [country.name, country.region]
    results = run_sql(sql, values)
    country.id = results[0]["id"]
    return country


def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        country = Country(row["name"], row["region"], row["id"])
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result["name"], result["region"], result["id"])
    return country


def update(country):
    pass
