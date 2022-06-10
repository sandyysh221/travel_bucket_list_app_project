import pdb

from models.attraction import Attraction
from models.city import City
from models.country import Country

import repositories.attraction_repository as attraction_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

country_1 = Country("Canada", "North America")
country_repository.save(country_1)

city_1 = City("Vancouver", country_1)
city_repository.save(city_1)

attraction_1 = Attraction("VanDusen Botanical Garden", "tower", city_1, "21 Feb")
attraction_repository.save(attraction_1)

pdb.set_trace()
