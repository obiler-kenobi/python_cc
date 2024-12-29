from random import randint

class Die:
    """A simple class to represent a die."""

    def __init__(self, sides=6):
        """Initialize the number of sides of a die"""
        self.sides = sides

    def roll_die(self):
        """Simulate rolling of a die"""
        rolled_face = randint(1, self.sides)
        return rolled_face
    
dice = Die()
results = []
for roll_num in range(10):
    results.append(dice.roll_die())

print(results)

dice = Die(10)
results = []
for roll_num in range(10):
    results.append(dice.roll_die())

print(results)

dice = Die(20)
results = []
for roll_num in range(10):
    results.append(dice.roll_die())

print(results)