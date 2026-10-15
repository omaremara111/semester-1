# Week 1.3, Session 1: For loop equivalent to a list comprehension

animals = ['dog','cat','hamster','goldfish']

not_fish_and_dog = [item for item in animals if item != 'goldfish' and item!= 'dog']

print(not_fish_and_dog)


# write the equivalent for loop to create the not_fish list from animals
# print your result to verify it is the same

