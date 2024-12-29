# NOTE: If the class you're writing is a specialized version of another 
# class you wrote, you can use inheritance. When one class inherits from 
# another, it takes on the attributes and methods of the first class. 
# The original class is called the parent class, and the new class is 
# the child class. The child class can inherit any or all of the 
# attributes and methods of its parent class, but it's also free to 
# define new attributes and methods of its own.

# NOTE: The __init__() method for a child class
# When you're writing a new class based on an existing class, you'll 
# often want to call the __init__() method from the parent class. This 
# will initialize any attributes that were defined in the parent 
# __init__() method and make them available in the child class.\

# electric_car.py

class Car:
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

# NOTE: The name of the parent class must be included in the parentheses
# in the definition of a child class.
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    # NOTE: The __init__() method takes in the information required to
    # make a Car instance
    def __init__(self, make, model, year):
        """Initialize attribtues of the parent class."""
        # NOTE: The super() function is a special function that allows
        # you to call a method from the parent class. This line tells
        # Python to call the __init__() method from Car, which gives an
        # ElectricCar instance all the attributes deffined in that
        # method.
        super().__init__(make, model, year)

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# NOTE: When you create a child class, the parent class must be part of 
# the current file and must appear before the child class in the file.

# NOTE: Defining Attributes and Methods for the Child Class
# Once you have a child class that inherits from a parent class, you can 
# add any new attributes and methods necessary to differentiate the 
# child class from the parent class.

class ElectricCar(Car): # V2
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attribtues of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()

# NOTE: Overriding methods from the Parent Class
# You can override any method from the parent class that doesn't fit 
# what you're trying to model with the child class. To do this, you 
# define a method in the child class with the same name as the mthod you 
# want to override in the parent class. Python will disregard the parent 
# class method and only pay attention to the method you define in the 
# child class.

class ElectricCar(Car): # V3
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attribtues of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    # This is an example assuming this method is also available in the 
    # Car class
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()

# NOTE: When you use inheritance, you can make your child classes retain 
# what you need and override anything you don't need from the parent 
# class.

# NOTE: Instances as Attributes
# When modeling something from the real world in code, you may find that 
# you're adding more and more detail to a class. You'll find that you 
# have a growing list of attributes and methods and that your files are 
# becoming lengthy. In these situations, you might recognize that part 
# of one class can be written as separate class. You can break your 
# large class into smaller classes that work together, this approach is 
# called composition.

class Battery:
    """A simple attempt to model a battery for an electri car."""

    def __init__(self, battery_size=40):
        """Initialize the batter's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This cas has a {self.battery_size}-kWh battery.")

class ElectricCar(Car): # V5
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attribtues of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

class Battery: #V2
    """A simple attempt to model a battery for an electri car."""

    def __init__(self, battery_size=40):
        """Initialize the batter's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This cas has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car): # V5
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attribtues of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
