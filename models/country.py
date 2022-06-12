class Country:
    def __init__(self, name, region, id=None, visited=False):
        self.name = name
        self.region = region
        self.id = id
        self.visited = visited

    def set_visited(self):
        self.visited = True
