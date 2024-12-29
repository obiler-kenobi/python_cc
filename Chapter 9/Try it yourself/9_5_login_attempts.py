class User:
    """A model that captures instructions for users"""

    def __init__(self, first_name, last_name, age, email):
        """Initialize user first name, last name, age, 
            and email attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increments the login attempts of the user by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the login attempts of the user"""
        self.login_attempts = 0

oliver = User('oliver john', 'arenas', 29, 'oliverjohn@gmail.com')
oliver.describe_user()
oliver.greet_user()

oliver.increment_login_attempts()
oliver.increment_login_attempts()
oliver.increment_login_attempts()
print(oliver.login_attempts)
oliver.reset_login_attempts()
print(oliver.login_attempts)