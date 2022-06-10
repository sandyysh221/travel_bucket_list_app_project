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
    pass


def select(id):
    pass


def update(country):
    pass
