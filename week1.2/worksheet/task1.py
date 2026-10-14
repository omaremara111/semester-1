# Worksheet 1.2: Task 1 Solution
mark = int(input("Please enter the mark out of 100 that you got: "))
if mark < 0 or mark > 100:
    print("Error: Grade must be an integer between 0 and 100")
    import sys
    sys.exit("Error!")

else:
    if mark<= 39:
        print(mark,"is a Fail")
    elif mark<=69:
        print(mark,"is a Pass")
    else:
        print(mark,"is a Distinction")

