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

    def add_city(self, name):
        city = City(name)
        self.cities.append(city)
        print(f"City {name} added")

    def add_neighbor(self, city_name, neighbor_name):
        city = next((c for c in self.cities if c.name == city_name), None)
        neighbor = next((c for c in self.cities if c.name == neighbor_name), None)
        if city and neighbor:
            city.neighbors.append(neighbor)
            print(f"{neighbor_name} added as a neighbor to {city_name}")
        else:
            print("One or both cities not found")

    