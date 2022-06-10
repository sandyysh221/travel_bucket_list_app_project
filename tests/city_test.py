import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City("Ottawa", 1)

    def test_city_has_name(self):
        self.assertEqual("Ottawa", self.city.name)

    def test_city_has_country_id(self):
        self.assertEqual(1, self.city.country_id)
