class Restaurant:
    """A class that models a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attribute"""
        self.restuarant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """A method that describes a restaurant"""
        print(f"Hello, this is the {self.restuarant_name.title()} and we specialize in {self.cuisine_type.title()} cuisines.")

    def open_restaurant(self):
        """A method that opens the restaurant"""
        print(f"Good Day! The {self.restuarant_name.title()} is now open to serve you the best {self.cuisine_type.title()} cuisines!")


restaurant = Restaurant('jollibee','filipino')

print(restaurant.restuarant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()