"""
This is the testing code for testing the triangle classification. It tests various combinations of 3 sides 
to see if they form a scalene, isosceles, or equilateral triangle. It also checks whether they form
a right triangle or not. Also, it checks to make sure that the sides form a valid triangle.

NOTE: If we import classify_triangle from triangleClassification.py, we should see all tests pass
OR import classify_triangle from buggyTriangles.py (with intentional bugs in the code) to see some failures. 

@author: amanda-zambrana
"""

import unittest

# from triangleClassification import classify_triangle
from buggyTriangles import classify_triangle

class triangleTest(unittest.TestCase):
    def test_scalene(self):
        self.assertEqual(classify_triangle(3,4,5), 'The triangle is scalene and a right triangle.')
        self.assertEqual(classify_triangle(3,4,6), 'The triangle is scalene, but not a right triangle.')

    def test_isosceles(self):
        self.assertEqual(classify_triangle(2,2,3), 'The triangle is isosceles, but not a right triangle.')

    def test_equilateral(self):
        self.assertEqual(classify_triangle(5,5,5), 'The triangle is equilateral, but not a right triangle.')

    def test_validTriangle(self):
        self.assertEqual(classify_triangle(2,3,10), 'The sides do not form a valid triangle.')


if __name__ == "__main__":
    classify_triangle(3,4,5)
    unittest.main(exit=False)
