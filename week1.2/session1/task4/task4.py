# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
#the item that is present in both sets will be outputed
both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
#because tomato is a repeated item in both sets so will only be included once
food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("raspberry")
print(fruit)

# Remove an item from vegetables
vegetables.discard("potato")
print(vegetables)

# Find and display symmetric difference of the two sets
print(fruit.symmetric_difference(vegetables))
