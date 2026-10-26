# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate
    
    # Add distance() method here
    def distance(self):
        """
        Returns the distance of this point from the origin (0, 0).
        """
        return math.hypot(self.x, self.y)
    
    # Add distance_to() method here
    def distance_to(self, other_point):
        """
        Returns distance from this point to another point.
        """
        return math.hypot(self.x - other_point.x, self.y - other_point.y)

    # (This will need a parameter representing another point)


# Finally, add code here to demonstrate use of Point
p1 = Point(3, 4)

print("X coordinate:", p1.x)
print("Y coordinate:", p1.y)
print("Distance from origin:", p1.distance())

p2 = Point(6, 8)

print("Distance to second point:", p1.distance_to(p2))
