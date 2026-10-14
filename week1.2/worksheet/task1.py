# Worksheet 1.2: Task 1 Solution
import sys

mark = input("Please enter the mark out of 100 that you got: ")

if not mark.isdecimal() or int(mark) > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

mark = int(mark)


if mark<= 39:
    print(mark,"is a Fail")
elif mark<=69:
    print(mark,"is a Pass")
else:
    print(mark,"is a Distinction")

