from db.run_sql import run_sql
from models.attraction import Attraction


def delete_all():
    sql = "DELETE FROM attractions"
    run_sql(sql)


def delete(id):
    pass


def save(attraction):
    sql = "INSERT INTO attractions (name, description, city_id, date) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [attraction.name, attraction.description, attraction.city.id, attraction.date]
    results = run_sql(sql, values)
    attraction.id = results[0]["id"]
    return attraction


def select_all():
    pass


def select(id):
    pass


def update(attraction):
    pass
