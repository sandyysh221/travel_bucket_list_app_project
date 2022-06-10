import pdb

from models.attraction import Attraction
from models.city import City
from models.country import Country

import repositories.attraction_repository as attraction_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

attraction_repository.delete_all()
city_repository.delete_all()
country_repository.delete_all()

country_1 = Country("Canada", "North America")
country_repository.save(country_1)
country_2 = Country("France", "Europe")
country_repository.save(country_2)
# country_repository.delete(1)
country_repository.select_all()

city_1 = City("Vancouver", country_1)
city_repository.save(city_1)
city_2 = City("Paris", country_2)
city_repository.save(city_2)
# city_repository.delete(1)
city_repository.select_all()

attraction_1 = Attraction("VanDusen Botanical Garden", "tower", city_1, "21 Feb")
attraction_repository.save(attraction_1)
attraction_2 = Attraction("Eiffle Tower", "tower", city_2, "19 Jun")
attraction_repository.save(attraction_2)
# attraction_repository.delete(2)
attraction_repository.select_all()

pdb.set_trace()
