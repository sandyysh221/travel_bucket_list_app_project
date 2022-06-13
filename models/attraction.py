class Attraction:
    def __init__(self, name, description, city, date, visited=False, id=None):
        self.name = name
        self.description = description
        self.city = city
        self.date = date
        self.visited = visited
        self.id = id

    def set_visited(self):
        self.visited = True
