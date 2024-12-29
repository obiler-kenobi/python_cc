ordinal_numbers = list(range(1,10))

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f"{ordinal_number}st") #print("1st"); book solution
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd") #print("2nd"); book solution
    elif ordinal_number == 3:
        print(f"{ordinal_number}rd") #print("3rd"); book solution
    else:
        print(f"{ordinal_number}th")