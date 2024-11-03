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

    def view_all_drivers(self):
        for driver in self.drivers:
            print(f"{driver.id}, {driver.name}, {driver.start_city}")

    def check_similar_drivers(self):
        city_drivers = {}
        for driver in self.drivers:
            if driver.start_city not in city_drivers:
                city_drivers[driver.start_city] = []
            city_drivers[driver.start_city].append(driver.name)
        
        for city, drivers in city_drivers.items():
            print(f"{city}: {', '.join(drivers)}")

        def show_cities(self):
        sorted_cities = sorted([city.name for city in self.cities], reverse=True)
        print(", ".join(sorted_cities))

    def search_city(self, key):
        matching_cities = [city.name for city in self.cities if key.lower() in city.name.lower()]
        print(", ".join(matching_cities))

    def print_neighboring_cities(self, city_name):
        city = next((c for c in self.cities if c.name == city_name), None)
        if city:
            neighbors = [neighbor.name for neighbor in city.neighbors]
            print(f"Neighbors of {city_name}: {', '.join(neighbors)}")
        else:
            print("City not found")

    def print_drivers_delivering_to_city(self, city_name):
        def can_reach_city(start_city, target_city, visited=None):
            if visited is None:
                visited = set()
            if start_city == target_city:
                return True
            visited.add(start_city)
            for neighbor in start_city.neighbors:
                if neighbor not in visited and can_reach_city(neighbor, target_city, visited):
                    return True
            return False

        target_city = next((c for c in self.cities if c.name == city_name), None)
        if target_city:
            delivering_drivers = [
                driver.name for driver in self.drivers
                if can_reach_city(next(c for c in self.cities if c.name == driver.start_city), target_city)
            ]
            print(f"Drivers delivering to {city_name}: {', '.join(delivering_drivers)}")
        else:
            print("City not found")

            