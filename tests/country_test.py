import unittest
from models.country import Country


class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("Canada", "North America", "CA", "Ottawa")

    def test_country_has_name(self):
        self.assertEqual("Canada", self.country.name)

    def test_country_has_region(self):
        self.assertEqual("North America", self.country.region)

    def test_country_has_capital(self):
        self.assertEqual("Ottawa", self.country.capital)

    def test_country_has_country_code(self):
        self.assertEqual("CA", self.country.code)

    def test_country_is_visited__false(self):
        self.assertEqual(False, self.country.visited)

    def test_country_is_visited__true(self):
        self.country.set_visited()
        self.assertEqual(True, self.country.visited)
