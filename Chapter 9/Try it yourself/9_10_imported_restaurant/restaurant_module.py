"Set of classes to represent restaurant"

class Restaurant:
    """A class that models a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attribute"""
        self.restuarant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """A method that describes a restaurant"""
        print(f"Hello, this is the {self.restuarant_name.title()} and we specialize in {self.cuisine_type.title()}.")

    def open_restaurant(self):
        """A method that opens the restaurant"""
        print(f"Good Day! The {self.restuarant_name.title()} is now open to serve you the best {self.cuisine_type.title()}!")

class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Initialize an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        # NOTE: This is the major difference in both solution
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
