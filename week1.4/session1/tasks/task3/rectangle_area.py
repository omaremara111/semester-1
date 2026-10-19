
# function implementation

def rectangle_area( ):  # define suitable input data
    # ...               # implement the function
    rec_length = int(input("Enter the length of the rectangle: "))
    rec_width = int(input("Enter the width of the rectangle: "))
    area = rec_length * rec_width
    print(f"Area of the rectangle is {area}")
    return              # return an appropriate value

# testing the function

#print(f"Area is {rectangle_area( )}")   # provide suitable data matching your inputs
rectangle_area()