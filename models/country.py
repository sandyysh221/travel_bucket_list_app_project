from models.countries_list import all_countries_list


class Country:
    def __init__(self, name, region, code, visited=False, id=None):
        self.name = name
        self.region = region
        self.code = code
        self.visited = visited
        self.id = id
        self.country_list = all_countries_list

    def set_visited(self):
        self.visited = True

    def get_country_by_name(self, country_to_find):
        for country in self.country_list:
            if country_to_find == country["name"]:
                return country
        return None

    def get_country_region(self, country_to_find):
        for country in self.country_list:
            if country_to_find == country["name"]:
                return country["continent"]
        return None
