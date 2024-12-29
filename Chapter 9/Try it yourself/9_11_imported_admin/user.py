"""A set of classes used to represent users, admins, and privileges"""

class User:
    """A model that captures instructions for users"""

    def __init__(self, first_name, last_name, age, email):
        """Initialize user first name, last name, age, 
            and email attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        """Prints a summary of the user's information"""
        print("\nInformation about this user:")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Greets the user"""
        name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Hello, {name}! Thank you for registering in our website!")

class Privileges:
    """A model for admin privileges"""

    def __init__(self, privileges=[]):
      self.privileges = privileges

    def show_privileges(self):
        """Shows the list of privilages of an administrator"""
        if self.privileges:
           for privilege in self.privileges:
               print(f"- {privilege}")
        else:
           print("- This user has no privileges.")

class Admin(User):
    """A subclass that models an administrator"""

    def __init__(self, first_name, last_name, age, email):
        """
        Initialize parent class attributes
        """
        super().__init__(first_name, last_name, age, email)
        self.privilege = Privileges()

