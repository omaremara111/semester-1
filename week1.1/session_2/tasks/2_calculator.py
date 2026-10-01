# Fill out the code to make a very simple calculator
try:
# ask the user to enter number1:
    number1 = int(input("Please enter number 1: "))

# ask the user to enter number 2:
    number2 = int(input("Please enter number 2: "))

# calculate the result of adding those numbers together
    result = number1 + number2

# print out the answer
    print(f"Answer is : {result}")

except:
    print("Please enter numbers only.")