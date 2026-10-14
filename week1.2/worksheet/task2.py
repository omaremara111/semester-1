# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
def read_numbers():
    line = input("Enter some float numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers
numbers = read_numbers()
print("Your list is:",numbers)

if not numbers:
    print("Erorr: no numbers provided")
    sys.exit(1)

#minimum:
minimum = min(numbers)
print("Minimum =",minimum)

#maximum:
maximum = max(numbers)
print("Maximum =",maximum)

#mean:
mean = sum(numbers) / len(numbers)
print("Mean =",mean)

#median:
sorted_numbers = sorted(numbers)
i = len(sorted_numbers)
if i % 2 == 1:
    median = sorted_numbers[i//2]
else:
    median =( (sorted_numbers[(i//2)-1]) + (sorted_numbers[(i//2)]) ) / 2

print("Median =",median)