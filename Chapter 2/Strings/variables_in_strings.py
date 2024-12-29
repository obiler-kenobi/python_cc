#Combining the first and last name and inserting it to string
#These strings are called f-strings where f stands for format.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

#Values become a list when both are inserted in the braces separated by comma
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name, last_name}"
print(full_name)

#Another example of f-string: Composing full messages using f-string
#Methods can also be used inside the f-string
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#Assigning f-string value to a variable
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)