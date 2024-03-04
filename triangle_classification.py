"""
This code is for the classification of triangles. It takes the 3 sides of
a triangle and determines whether it is equilateral, isosceles, or scalene.
It also determines whether or not it is a right triangle.
Also, if the 3 sides do not form a valid triangle, it returns that info.

@author: amanda-zambrana
"""


def classify_triangle(side_a, side_b, side_c):
    """
    This function is used to classify a triangle based on the lengths of its 3 sides.

    Parameters:
    side_a: Length of side a of the triangle.
    side_b: Length of side b of the triangle.
    side_c: Length of side c of the triangle.

    Returns:
    str: A string describing the type of triangle.
    """

    # The triangle inequality theorem states that sum of 2 sides must be greater than the third side
    if side_b + side_c > side_a and side_a + side_c > side_b and side_a + side_b > side_c:
        if side_a == side_b and side_b == side_c:
            # Equilateral triangles by nature cannot be right triangles
            return "The triangle is equilateral, but not a right triangle."
        if side_a == side_b or side_b == side_c or side_a == side_c:
            if side_a**2 + side_b**2 == side_c**2 or side_b**2 + side_c**2 == side_a**2 \
                or side_a**2 + side_c**2 == side_b**2:
                return "The triangle is isosceles and a right triangle."
            return "The triangle is isosceles, but not a right triangle."
        if side_a != side_b and side_b != side_c and side_a != side_c:
            if side_a**2 + side_b**2 == side_c**2 or side_b**2 + side_c**2 == side_a**2 \
                or side_a**2 + side_c**2 == side_b**2:
                return "The triangle is scalene and a right triangle."
            return "The triangle is scalene, but not a right triangle."
    return "The sides do not form a valid triangle."


# test cases with different side lengths to see if the code is functioning correctly
print(classify_triangle(3,4,5)) # scalene & right
print(classify_triangle(2,2,3)) # isosceles & not right
print(classify_triangle(5,5,5)) # equilateral & not right
print(classify_triangle(2,3,10)) # not a valid triangle
