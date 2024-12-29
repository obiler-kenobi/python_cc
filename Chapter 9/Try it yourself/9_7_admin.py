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

class Admin(User):
    """A subclass that models an administrator"""

    def __init__(self, first_name='admin', last_name='admin', age=0, 
                 email='admin@gmail.com'):
        """
        Initialize parent class attributes
        Then initialize the privilege attribute specific for administrators
        """
        super().__init__(first_name, last_name, age, email)
        self.privileges = []

    def show_privileges(self):
        """Shows the list of privilages of an administrator"""
        print(f"The administrator can:")
        for privilege in self.privileges:
            print(f" - {privilege}")


# book sample
# eric = Admin('eric','matthes', 25, 'e_matthes@example.com')
admin = Admin()
admin.greet_user()
admin.privileges = [
    "can add post", 
    "can delete post", 
    "can ban user"
    ]

admin.show_privileges()