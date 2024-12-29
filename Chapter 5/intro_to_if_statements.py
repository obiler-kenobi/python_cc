#if statements allows you to examine the current state of a program and
#respond appropriately to that state

#ex. car names are proper names that's why it should printed in title
#case, however 'bmw' should be printed in uppercase. The program below
#loops through the list and looks for the value 'bmw' and prints it in
#uppercase while the other car names will be printed in title case.
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#conditional tests are expressions that can be evaluated as True or
#False. Python uses the the value True and False to decide whether the 
#code in an if statement should be be executed.

#Checking for equality: most conditional tests compare values of a
#variable to a specific value. The simplest conditional test checks
#whether a value of a variable is equal to the value of interest.

#== - 'Equality operator': this returns True if the values on the left
#and right side of the operator match and False if they don't. Testing 
#for equality is case sensitive. Values with different capitalization 
#are not considered equal: 'audi' != 'Audi'

#If you want to test only for the value of the variable and the case 
#doesn't matter, you can convert the variable's (or the comparison
#value) value to lowercase before doing the comparison, the lower()
#method does not change the value that was originally stored in car
car = 'Audi'
print(car.lower() == 'audi')

#Checking for inequality: when you want to determine whether two values
#are not equal, we use the != operator.
request_topping = 'mushrooms'

if request_topping != 'anchovies':
    print("Hold the anchovies!")

#Numerical comparisons:
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

#other examples of numerical comparisons:
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

#multiple conditions: 'and' and 'or'
#'and'
#We use 'and' to check whether two conditions are both True
#simultaneously. If either or both test fail, the expression evaluates
#to false.
print("\n")
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

#To improve readability:
#(age_0 >= 21) and (age_1 >= 21)

#'or'
#'or' allows us to check multiple conditions as well, but it passes
#when either or both of the individual tests pass. It only fails when
#both tests fail.
print("\n")
age_0 = 22
age_1 = 18
print((age_0 >= 21) or (age_1 >= 21))
age_0 = 18
print((age_0 >= 21) or (age_1 >= 21))
