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
        
    def add_driver(self, name, start_city):
        driver_id = f"ID{self.next_id:03d}"
        self.next_id += 1
        driver = Driver(driver_id, name, start_city)
        self.drivers.append(driver)
        print(f"Driver {name} added with ID {driver_id}")
    
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

    def drivers_menu(self):
        while True:
            print("\nDrivers Menu:")
            print("1. View all drivers")
            print("2. Add a driver")
            print("3. Check similar drivers")
            print("4. Go back to the main menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_all_drivers()
            elif choice == '2':
                name = input("Enter driver name: ")
                start_city = input("Enter start city: ")
                if start_city not in [city.name for city in self.cities]:
                    add_city = input("City not found. Do you want to add it? (y/n): ")
                    if add_city.lower() == 'y':
                        self.add_city(start_city)
                    else:
                        continue
                self.add_driver(name, start_city)
            elif choice == '3':
                self.check_similar_drivers()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def cities_menu(self):
        while True:
            print("\nCities Menu:")
            print("1. Show cities")
            print("2. Search city")
            print("3. Print neighboring cities")
            print("4. Print drivers delivering to city")
            print("5. Go back to the main menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.show_cities()
            elif choice == '2':
                key = input("Enter search key: ")
                self.search_city(key)
            elif choice == '3':
                city = input("Enter city name: ")
                self.print_neighboring_cities(city)
            elif choice == '4':
                city = input("Enter city name: ")
                self.print_drivers_delivering_to_city(city)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def main_menu(self):
        while True:
            print("\nHello! Please enter:")
            print("1. To go to the drivers' menu")
            print("2. To go to the cities' menu")
            print("3. To exit the system")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.drivers_menu()
            elif choice == '2':
                self.cities_menu()
            elif choice == '3':
                print("Thank you for using WeDeliver. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

system = WeDeliver()

# Add some initial data
system.add_city("Akkar")
system.add_city("Saida")
system.add_city("Jbeil")
system.add_city("Beirut")
system.add_city("Zahle")

system.add_neighbor("Akkar", "Beirut")
system.add_neighbor("Saida", "Beirut")
system.add_neighbor("Jbeil", "Beirut")
system.add_neighbor("Jbeil", "Zahle")

system.add_driver("Max Verstappen", "Akkar")
system.add_driver("Charles Leclerc", "Saida")
system.add_driver("Lando Norris", "Jbeil")

# Run the main menu
system.main_menu()