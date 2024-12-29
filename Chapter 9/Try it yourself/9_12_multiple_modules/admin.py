"""Set of classes used to represent admin and privileges"""
from user import User

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

