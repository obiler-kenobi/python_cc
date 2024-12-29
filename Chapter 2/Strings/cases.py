# NOTE: Changing case of text into title case
# This is usually helpful when the program needs to recognize input of users as the same, ex: ADA, Ada, ada will all be equal to Ada when used with .title(). 
# Lowercase and uppercase can also be used and will have similar effect. 
# [.lower(), .upper()]
name = "ada lovelace"
print(name.title())

#lowercase
#Usually useful for storing data since developers can't trust the capitalization the users provide
name = "ADA LOVELACE"
print(name.lower())

#UPPERCASE
name = "ada lovelace"
print(name.upper())