import random

# Get user to input how many random numbers they want
number = int(input("How many random numbers would you like? "))

# Generate this many random numbers
numbers = [random.randint(1, 100) for _ in range(number)]

# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as outfile:
    for random_number in numbers:
        outfile.write(f"{random_number}\n")
