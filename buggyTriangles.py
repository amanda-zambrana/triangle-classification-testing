""" 
This code is written for the classification of triangles. It is intended to 
take the 3 sides of a triangle and determine whether it is equilateral, 
isosceles, or scalene. It also determines whether it is a right triangle. 

NOTE: * This version of the code is written with the intentional inclusion 
of bugs to be detected with the testing code in testingTriangleClass.py * 

@author: amanda-zambrana
"""


def classify_triangle(a,b,c):
    if b + c > a and a + c > b and a + b > c: # triangle inequality theorem states that sum of 2 sides must be greater than the third side
        
        # Below is an intentional bug, stating that sides 2,2,3 create an equilateral triangle, when they do not (should be isosceles)
        if a == 2 and b == 2 and c == 3:
            return "The triangle is equilateral, but not a right triangle." # this should fail when we run testing code
        
        # Below is an intentional bug, stating that sides 3,4,5 create a scalene but not right triangle, when they actually make a scalene AND right triangle 
        if a == 3 and b == 4 and c == 5:
            return "The triangle is scalene, but not a right triangle." # this should fail when we run testing code
        
        if a == b and b == c:
            return "The triangle is equilateral, but not a right triangle."  # equilateral triangles by nature cannot be right triangles
        elif a == b or b == c or a == c:
            if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
                return "The triangle is isosceles and a right triangle."
            else:
                return "The triangle is isosceles, but not a right triangle."
        elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return "The triangle is scalene and a right triangle."
        else: 
            return "The triangle is scalene, but not a right triangle."
    else: 
        return "The sides do not form a valid triangle."


if __name__ == "__main__":
    a, b, c = map(int, input("Please enter the 3 side lengths for the triangle triangle (split by commas ','): ").split(","))
    classify_triangle(a,b,c)
