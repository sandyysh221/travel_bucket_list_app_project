class City:
    def __init__(self, name, country, id=None, visited=False):
        self.name = name
        self.country = country
        self.id = id
        self.visited = visited

    def set_visited(self):
        self.visited = True
