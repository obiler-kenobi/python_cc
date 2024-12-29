my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite food are:")
for food in my_foods:
    print(f"- {food.title()}")

print("\nMy friend's favorite food are:")
for food in friend_foods:
    print(f"- {food.title()}")