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
    """A subclass that models an Ice Cream Stand"""

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        """
        Initialize attributes of the parent class
        Then initialize the flavors attribute specific to the 
        ice cream stand
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Prints the flavors available in the ice cream stand."""
        print("These are the available flavors:")
        for flavor in self.flavors:
            print(flavor)

ice_cream_stand = IceCreamStand('selecta','ice cream', 'chocolate',
                                 'strawberry', 'oreo', 'vanilla')

ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.display_flavors()

# BOOK SOLUTION
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


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()