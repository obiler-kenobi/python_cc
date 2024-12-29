topping = ""

prompt = "Enter 'quit' to stop the program."
prompt += "\nWhat topping/s do you want to add in your pizza? "

active = True
while active:
    topping = input(prompt)

    if topping != 'quit':
        print(f"\n{topping.title()} is added to yours pizza!\n")
    else:
        active = False


# book solution

# while True:
#   topping = input(prompt)
#   
#   if topping != 'quit':
#       print(f"\n{topping.title()} is added to your pizza!\n")
#   else:
#       break