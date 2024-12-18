class Car:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def display_car_details(self):
        print(f"Car Name: {self.name}")
        print(f"Model: {self.color}")
        print(f"Price: ${self.price}")

class CarCompany:
    def __init__(self):
        # Create car objects for the company
        self.cars = [
            Car("hyundai", "red", 25000),
            Car("toyota", "green", 30000),
            Car("", "yellow", 35000)
        ]

    def print_car_details(self):
        print("Car Company Details:\n")
        for car in self.cars:
            car.display_car_details()
            print("-" * 20)

# Create an object of CarCompany
company = CarCompany()

# Print the car details using the method
company.print_car_details()
