import unittest
from models.country import Country


class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("Canada", "North America")

    def test_country_has_name(self):
        self.assertEqual("Canada", self.country.name)

    def test_country_has_region(self):
        self.assertEqual("North America", self.country.region)

    # def test_country_has_city(self):
    #     self.country.find_city_in_country(country)
    #     self.assertEqual("Tokyo", self.country.country_cities)
