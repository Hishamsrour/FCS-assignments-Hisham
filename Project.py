class Driver:
    def __init__(self, id, name, start_city):
        self.id = id
        self.name = name
        self.start_city = start_city

class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

class WeDeliver:
    def __init__(self):
        self.drivers = []
        self.cities = []
        self.next_id = 1