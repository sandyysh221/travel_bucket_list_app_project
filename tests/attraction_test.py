import unittest
from models.attraction import Attraction


class TestAttraction(unittest.TestCase):
    def setUp(self):
        self.attraction = Attraction(
            "Canada's Wonderland", "Amusement Park", 1, "1 July"
        )

    def test_attraction_has_name(self):
        self.assertEqual("Canada's Wonderland", self.attraction.name)

    def test_attraction_has_description(self):
        self.assertEqual("Amusement Park", self.attraction.description)

    def test_attraction_has_city_id(self):
        self.assertEqual(1, self.attraction.city)

    def test_attraction_has_date(self):
        self.assertEqual("1 July", self.attraction.date)

    def test_attraction_has_visited__false(self):
        self.assertEqual(False, self.attraction.visited)

    def test_attraction_has_visited__true(self):
        self.attraction.set_visited()
        self.assertEqual(True, self.attraction.visited)
