class Employee:
    """Store employee details and give a raise."""
    def __init__(self, first_name, last_name, annual_salary):
        """Store employee name and salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Give employee raise."""
        self.annual_salary += raise_amount