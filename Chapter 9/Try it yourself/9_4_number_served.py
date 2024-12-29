class Restaurant:
    """A class that models a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attribute"""
        self.restuarant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """A method that describes a restaurant"""
        print(f"Hello, this is the {self.restuarant_name.title()} and we specialize in {self.cuisine_type.title()} cuisines.")

    def open_restaurant(self):
        """A method that opens the restaurant"""
        print(f"Good Day! The {self.restuarant_name.title()} is now open to serve you the best {self.cuisine_type.title()} cuisines!")

    def set_number_served(self, number_of_customers):
        """Lets the user set the number of customers served."""
        self.number_served = number_of_customers

    def increment_number_served(self, total_customers):
        """Lets the program increment the number of customers served."""
        self.number_served += total_customers

restaurant = Restaurant('jollibee','filipino')
print(restaurant.number_served)
restaurant.number_served = 5
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(100)
print(restaurant.number_served)