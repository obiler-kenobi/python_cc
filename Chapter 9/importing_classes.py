# NOTE: Python lets you store classes in modules and then import classes 
# you need into your main program.

# NOTE: Importing a single class
# We can create a module containing just the Car class

# NOTE: The import statement tell Python to open the car module and 
# import the class Car
from car_module import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# NOTE: Importing a class is an effective way to program. When you move 
# the class to a module and import the module, you still get all the 
# same functionality, but you ,eep your main program file clean and easy 
# to read. You also store most of the logic in separate files; once your 
# classes work as you want them to, you can leave those files alon and 
# focus on the higher-level logic of your main program.

# NOTE: Storing multiple classes in a module
# You can store as many classes as you need in a single module, although 
# each class in a module should be related somehow.

from car_module_2 import ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

# NOTE: Importing multiple classes from a module
# You can import as many classes as you need into a program file.

from car_module_2 import Car, ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# NOTE: You can import multiple classes from a module by separating each 
# class with a comma.

# NOTE: Importing an entire module
# You can also import an entire module and then access the classes you 
# need using dot notation. This approach is simple and results in code 
# that is easy to read. Because every call that creates an isntance of a 
# class includes the module name, you won't have naming conflicts with 
# any names used in the current file.

import car_module_2

my_mustang_2 = car_module_2.Car('ford', 'mustang', 2024)
print(my_mustang_2.get_descriptive_name())
my_leaf_2 = car_module_2.Car('nissan', 'leaf', 2024)
print(my_leaf_2.get_descriptive_name())

# NOTE: Importing all classes from a module
# You can import every class from a module however, this method is not 
# recommended for two reasons.
# 1) It's helpful to be able to read the import statements at the top 
# of a file and get a clear sense of which classes a program uses. With 
# this approach it's unclear which classes you're using from the module. 
# 2) This approach can also lead to confusion with names in the file. If 
# you accidentally import a class with the same name as something else 
# in you're program file, you can create errors that are hard to 
# diagnose.

# NOTE: Syntax from module_name import *

# NOTE: If you need to import many classes from a module, you're better 
# off importing the entire module and using the module_name.ClassName 
# syntax.

# NOTE: Importing a module into a module
# Sometimes you'll want to spread out your classes over several modules 
# to keep any one file from growing too large and avoid storing 
# unrelated classes in the same module. When you store your classes in 
# several modules, you may find that a class in one module depends on a 
# class in another module.When this happens, ou can import the required 
# class into the first module.

# see electric_car_module.py for example

from car_module import Car
from electric_car_module import ElectricCar

my_mustang_3 = Car('ford3', 'mustang', 2024)
print(my_mustang_3.get_descriptive_name())

my_leaf_3 = ElectricCar('nissan3', 'leaf', 2024)
print(my_leaf_3.get_descriptive_name())

# NOTE: Using aliases
# Aliases can be helpful when using modules to organize your project's code. You can use alases when importing classes as well.

from electric_car_module import ElectricCar as EC
my_leaf4 = EC('nissan4', 'leaf', 2024)
print(my_leaf4.get_descriptive_name())

# NOTE: You can also give a module an alias
import electric_car_module as ecm
my_leaf5 = ecm.ElectricCar('nissan5', 'leaf', 2024)
print(my_leaf5.get_descriptive_name())