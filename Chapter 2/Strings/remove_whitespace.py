#NOTE: It can only be seen on python terminal

#rstrip(): Removing whitespaces in the right
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())

#remove whitespace permanently
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

#remove whitespace from left side
favorite_language = ' python'
favorite_language = favorite_language.lstrip()
print(favorite_language)

#remove whitespace from both side
favorite_language = ' python '
favorite_language = favorite_language.strip()
print(favorite_language)