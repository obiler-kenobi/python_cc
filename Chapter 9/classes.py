# NOTE: Object-oriented programming (OOP) is one of the most effective
# approaches to writing software. In object-oriented programming, you
# write classes that represent real-world things and situations, and you
# create objects based on these classes. When you write a class, you
# define the general behavior that a whole category of objects can have.

# NOTE: When you create individual objects from the class, each object
# is automatically equipped with the general behavior; you can then give
# each object whaterver unique traits you desire.

# NOTE: Making an object from a class is called instatiation, and you
# work with instances of a class.

# NOTE: Creating and using a class
# You can model almost anything using classes.

# NOTE: Creating the Dog Class
class Dog:
    """A simple attempt to madel a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

# NOTE: By convention, capitalized names refer to classes in Python

# NOTE: The __init__() Method
# A function that's part of a class is a method. Everything you learned
# about functions applies to methods as well; the only practical
# difference for now is the way we'll call methods.

# NOTE: The __init__() method is a special method that Python runs
# automatically whenever we create a new instance based on the class

# NOTE: This method has two leading underscores and two trailing
# underscores, a convention that helps prevent Python's default method 
# names from conflicting with your method names

# NOTE: We define the __init__() method to have three parameters: self,
# name, and age.

# NOTE: Self
# The self parameter is required in the method definition, and it must
# come first, before the other parameters. This must be included in the 
# definition because when Python calls this metho later (to create an 
# instance of Dog), the method will call automatically pass the self
# argument.

# NOTE: Every method call associated with an instance automatically
# passes self, which is a reference to instance itself; it gives the
# individual instance access to the attributes and methods in the class

# NOTE: The two variables defined in the body of the __init__() method
# each have the prefix self. Any variable prefixed with self is
# available to every method in the class, and we'll also be able to
# access these variables through any instance created from the class

# NOTE: The line self.name = name takes the value associated with the 
# parameter name and assigns it to the variable name (self.name), which 
# is then attached to the instance (self) being created. Variables that
# are accessible through instances like this are called attributes

# NOTE: The Dog class has two other methods defined: sit() and
# roll_over(). The instances that will be created will also have access
# to these methods.

# NOTE: Making an instance from a class
# Think of a class as a set of instructions for how to make an instance.
# The Dog class is a set of instructions that tells Python how to make
# individual instances representing specific dogs

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# NOTE: This example tells Python to create a dog (instance) whose name
# is 'Willie' nad whose age is 6. When Python reads this line, it calls
# the __init__() method in Dog with arguments 'Willie' and 6.

# NOTE: The __init__() method creates an instance representing this
# particular dog and sets the name and age attributes using the values 
# we provided

# NOTE: Python then returns an instance representing this dog. we assign
# that instance to the variable my_dog. The naming convention is helpful
# here; we can usually assume that a capitalize name like Dog refers to
# a class, and a lowercase name like my_dog refers to a single instance 
# created from a class

# NOTE: Accessing Attributes
# To access the attributes of an instance, you use dot notation.
# ex. my_dog.name

# NOTE: Dot notation is used often in Python. This syntax demonstrates
# how Python finds an attribute's value. In the example, Python looks at
# the instance my_dog and then finds the attribute name associated with
# the instance. This is the same attribute referred to as self.name in
# class Dog.

# NOTE: Calling methods
# After we create an instance from the class Dog, we can use dot 
# notation to call any method defined in Dog

my_dog.sit()
my_dog.roll_over()

# NOTE: To call a method, give the name of the instance (my_dog) and the
# method you want to call, separated by a dot. When Python reads
# my_dog.sit(), it looks for the method sit() in the class Dog and runs
# that code.

# NOTE: Creating multiple instances
# You can create as many instances from a class as you need

your_dog = Dog('Lucy',3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# NOTE: In this example we create a dog named Willie and a dog named
# Lucy. Each dog is a separate instance with its own set of attributes,
# capable of the same set of actions

# NOTE: Even if we used the same name and age for the second dog, Python
# will still create a separate instance from the Dog class. You can make
# as many  instances from one class as you need, as long as you give
# each instance a unique variable name or it occupies a unique spot in a
# list or dictionary