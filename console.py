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

country_1 = Country("Japan", "Asia", "JP")
country_repository.save(country_1)
country_2 = Country("Peru", "South America", "PE")
country_repository.save(country_2)
country_3 = Country("United Kingdom", "Europe", "GB", True)
country_repository.save(country_3)
# country_repository.delete(1)
country_repository.select_all()

city_1 = City("Kyoto", country_1)
city_repository.save(city_1)
city_2 = City("Cuzco", country_2)
city_repository.save(city_2)
city_3 = City("Edinburgh", country_3)
city_repository.save(city_3)
city_4 = City("London", country_3, True)
city_repository.save(city_4)
# city_repository.delete(1)
city_repository.select_all()

attraction_1 = Attraction("Fushimi Inari Shrine", "Shinto shrine", city_1, "13 Aug")
attraction_repository.save(attraction_1)
attraction_2 = Attraction("Machu Picchu", "Incan citadel", city_2, "19 Jun")
attraction_repository.save(attraction_2)
# attraction_repository.delete(2)
attraction_repository.select_all()

# country_repository.find_city_in_country(country_1)

pdb.set_trace()
