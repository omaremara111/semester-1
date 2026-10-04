"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
monthlysaving = input("Please enter the amount of money you wish to save every month. This should be a whole number: ")

while not monthlysaving.isdigit():
    monthlysaving = input("Invalid Amount, try again. Should be an integer: ")

monthlysaving = int(monthlysaving)

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
yearlysaving = monthlysaving * 12
print(f"Your yearly savings will be: £{yearlysaving}")


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

intrest = yearlysaving * 0.008
totalsaving = yearlysaving + intrest
print(f"Your total yearly savings with inrest is : £{totalsaving:.2f}")
