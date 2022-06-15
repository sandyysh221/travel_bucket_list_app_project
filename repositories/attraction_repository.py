from db.run_sql import run_sql
from models.attraction import Attraction

import repositories.city_repository as city_repository


def delete_all():
    sql = "DELETE FROM attractions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM attractions WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def save(attraction):
    sql = "INSERT INTO attractions (name, description, city_id, date, visited) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [
        attraction.name,
        attraction.description,
        attraction.city.id,
        attraction.date,
        attraction.visited,
    ]
    results = run_sql(sql, values)
    attraction.id = results[0]["id"]
    return attraction


def select_all():
    attractions = []
    sql = "SELECT * FROM attractions"
    results = run_sql(sql)
    for row in results:
        city = city_repository.select(row["city_id"])
        attraction = Attraction(
            row["name"],
            row["description"],
            city,
            row["date"],
            row["visited"],
            row["id"],
        )
        attractions.append(attraction)
    return attractions


def select(id):
    attraction = None
    sql = "SELECT * FROM attractions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        city = city_repository.select(result["city_id"])
        attraction = Attraction(
            result["name"],
            result["description"],
            city,
            result["date"],
            result["visited"],
            result["id"],
        )
    return attraction


def update(attraction):
    sql = "UPDATE attractions SET (name, description, city_id, date, visited) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [
        attraction.name,
        attraction.description,
        attraction.city.id,
        attraction.date,
        attraction.visited,
        attraction.id,
    ]
    run_sql(sql, values)


def find_attraction_by_name(city):
    searched_attraction = []
    sql = "SELECT * FROM attractions WHERE name = %s"
    values = [city]
    results = run_sql(sql, values)
    for row in results:
        city = city_repository.select(row["city_id"])
        attraction = Attraction(
            row["name"],
            row["description"],
            city,
            row["date"],
            row["visited"],
            row["id"],
        )
        searched_attraction.append(attraction)
    return searched_attraction
