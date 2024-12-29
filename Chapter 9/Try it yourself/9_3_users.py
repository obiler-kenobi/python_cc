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

oliver = User('oliver john', 'arenas', 29, 'oliverjohn@gmail.com')
oliver.describe_user()
oliver.greet_user()

frances = User('frances mae', 'aterrado', 22, 'francesmae@gmail.com')
frances.describe_user()
frances.greet_user()

jr = User('john rey', 'sergio', 28, 'johnrey@gmail.com')
jr.describe_user()
jr.greet_user()

leslie = User('leslie', 'zaldua', 26, 'leslie@gmail.com')
leslie.describe_user()
leslie.greet_user()