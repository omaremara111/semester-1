# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")
#States the orginal string
print(f"\nOriginal String: {user_string}")
#Converts sting to lowercase
print(f"Modified String 1: {user_string.lower()}")
#Converts sting to uppercase
print(f"Modified String 2: {user_string.upper()}")
#Removes any spaces from string
print(f"Modified String 3: {user_string.strip()}")
#Replaces the letter 'a' in the string to '@'
print(f"Modified String 4: {user_string.replace('a', '@')}")
#Capatilizes the first letter in the string
print(f"Modified String 5: {user_string.capitalize()}")
#Reverses the string
print(f"Modified String 6: {user_string[::-1]}")
#First letter of string is capatalised
print(f"Modified String 7: {user_string.title()}")
#Outputs the length of the string(number of characters)
print(f"Modified String 8: {len(user_string)}")
#Finds the index of the first 'a' in the string
print(f"Modified String 9: {user_string.find('a')}")
#Outputs the number of times 'a' is found in the string
print(f"Modified String 10: {user_string.count('a')}")
#Checks if the string starts with 'Hello'
print(f"Modified String 11: {user_string.startswith('Hello')}")
#Checks if the string ends with '!'
print(f"Modified String 12: {user_string.endswith('!')}")
#Checks if the string is alphanumeric
print(f"Modified String 13: {user_string.isalnum()}")
#Checks if all the characters in the string are alphabetic
print(f"Modified String 14: {user_string.isalpha()}")
#Checks if all the characters in the string are digits
print(f"Modified String 15: {user_string.isdigit()}")



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!