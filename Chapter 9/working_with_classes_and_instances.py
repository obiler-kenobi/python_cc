# NOTE: You can use classes to represent many real-world situations.
# When writing classes, you'll spend most of your time working with 
# instances created from that class. One of the first tasks you'll want 
# to do is modify the attributes with a particular instance.

# NOTE: You can modify the attributes of an instance directly or write 
# methods that update attributes in specific ways.

# The Car class
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# Setting a Default Value for an attribute
# NOTE: When an instance is created, attributes can be defined without 
# being passed in as parameters. These attributes can be defined in the 
# __init__() method, where they are assigned a default value.

class Car: #V2
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
            
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying Attribute Values
# NOTE: You can change an attribute's value in three ways: you can 
# change the value directly through an instance, set the value through a
# method, or increment the value (add a certain amount to it) through 
# a method.

# Modifying an Attribute's Value directly
# NOTE: We use dot notation to access the car's odometer_reading 
# attribute, and set its value directly.

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an Attribute's Value through a method
# NOTE: It can be helpful to have methods that update certain attributes 
# for you. Instead of accessing the attributes directly, you pass the 
# new value to a method that handles the updating internally.

class Car: #V3
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_new_car = Car('audi','a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(29)
my_new_car.read_odometer()

class Car: #V4
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi','a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(29)
my_new_car.read_odometer()
my_new_car.update_odometer(30)
my_new_car.read_odometer()

# Incrementing an Attribute's value through a method
# NOTE: Sometimes you'll want to increment an attribute's value by a 
# certain amount, rather than set an entirely new value.

class Car: #V5
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# NOTE: You can use methods like this to control how users of your 
# program update values such as an odometer reading, but anyone with 
# access to the program can set the odometer reading to any value by 
# accessing the attribute directly. Effective security takes extreme 
# attention to detail in addition to basic checks like those shown here.

