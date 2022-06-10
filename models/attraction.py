class Attraction:
    def __init__(self, name, description, city_id, date, id=None, visited=False):
        self.name = name
        self.description = description
        self.city_id = city_id
        self.date = date
        self.id = id
        self.visited = visited

    def set_visited(self):
        self.visited = True
