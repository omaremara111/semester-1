# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)

        if not isinstance(self.width, (int, float)):
            raise TypeError("Width must be a number")

        if not isinstance(self.height, (int, float)):
            raise TypeError("Height must be a number")

        if not (self.width > 0):
            raise ValueError("Width must be greater than 0")

        if not (self.height > 0):
            raise ValueError("Height must be greater than 0")

    def is_square(self):
        """
        Returns True if the rectangle is a square, False otherwise.
        """
        return self.width == self.height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    