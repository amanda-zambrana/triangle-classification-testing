""" 
This code is for the classification of triangles. It takes the 3 sides of
a triangle and determines whether it is equilateral, isosceles, or scalene. 
It also determines whether or not it is a right triangle. 
Also, if the 3 sides do not form a valid triangle, it returns that info. 

@author: amanda-zambrana
"""

def classify_triangle(a, b, c):
    if b + c > a and a + c > b and a + b > c: # triangle inequality theorem states that sum of 2 sides must be greater than the third side
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


# test cases with different side lengths to see if the code is functioning correctly 
classify_triangle(3,4,5) # scalene & right 
classify_triangle(2,2,3) # isosceles & not right
classify_triangle(5,5,5) # equilateral & not right
classify_triangle(2,3,10) # not a valid triangle
