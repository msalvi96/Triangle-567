# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        """ Test For Right Angled Triangles """
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertNotEqual(classify_triangle(1, 1, 3), "Right", '1,1,3 is not a Right triangle')

    def testEquilateralTriangleA(self):
        """ Test for Equilateral Triangles """
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classify_triangle(4, 4, 8), 'Equilateral', '4,4,5 is not an Equilateral Triangle')
        
    def testIsoscelesTriangleA(self):
        """ Test for Isoceles Triangles """
        self.assertEqual(classify_triangle(4, 8, 4), 'Isosceles', '4,8,4 is an Isosceles Triangle')
        self.assertEqual(classify_triangle(4, 4, 8), 'Isosceles', '4,4,8 is an Isosceles Triangle')
        self.assertEqual(classify_triangle(8, 4, 4), 'Isosceles', '8,4,4 is an Isosceles Triangle')
        self.assertNotEqual(classify_triangle(3, 6, 5), 'Isosceles', '3,6,5 is not an Isosceles Triangle')
        self.assertNotEqual(classify_triangle(3, 3, 3), 'Isosceles', '3,3,3 is not an Isosceles Triangle')        

    def testScaleneTriangleA(self):
        """ Test for Scalene Triangles """
        self.assertEqual(classify_triangle(4, 5, 6), 'Scalene', '4,5,6 is a Scalene Triangle')
        self.assertNotEqual(classify_triangle(3, 3, 5), 'Scalene', '3,3,5 is not a scalene triangle')
        self.assertNotEqual(classify_triangle(3, 5, 3), 'Scalene', '3,5,3 is not a scalene triangle')
        self.assertNotEqual(classify_triangle(5, 3, 3), 'Scalene', '3,4,5 is not a scalene triangle')
        self.assertNotEqual(classify_triangle(3, 4, 5), 'Scalene', '3,4,5 is not a scalene triangle')

    def testInvalidTriangleA(self):
        """ Negative Tests """
        self.assertEqual(classify_triangle('One', 2, 3), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle('One', 'Two', 3), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle('One', 'Two', 'Three'), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(2.136, 5, 6), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(0, 12, 12), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(3, 0, 3), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(4, 4, 0), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(-1, 1, 2), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(-2, -1, 2), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(2, -2, 3), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(3, -2, -1), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(-3, -2, -1), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(250, 120, 150), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(20, 180, 250), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(350, 450, 550), 'InvalidInput', 'Invalid Input')
        self.assertEqual(classify_triangle(350, 150, 250), 'InvalidInput', 'Invalid Input')

    def testInvalidTriangleB(self):
        """ Negative Tests """
        self.assertEqual(classify_triangle(1, 10, 12), 'NotATriangle', 'Sum of 2 sides not greater than or equal to third side')
        self.assertEqual(classify_triangle(3, 16, 12), 'NotATriangle', 'Sum of 2 sides not greater than or equal to third side')
        self.assertEqual(classify_triangle(25, 10, 12), 'NotATriangle', 'Sum of 2 sides not greater than or equal to third side')
        self.assertEqual(classify_triangle(2, 25, 95), 'NotATriangle', 'Sum of 2 sides not greater than or equal to third side')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
