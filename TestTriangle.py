# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertNotEqual(classifyTriangle(1, 1, 3), "Right", '1,1,3 is not a Right triangle')
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertNotEqual(classifyTriangle(4, 4, 8), 'Equilateral', '4,4,5 is not an Equilateral Triangle')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(4, 8, 4), 'Isosceles', '4,8,4 is an Isosceles Triangle')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(4, 4, 8), 'Isosceles', '4,4,8 is an Isosceles Triangle')

    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(8, 4, 4), 'Isosceles', '8,4,4 is an Isosceles Triangle')

    def testIsoscelesTriangleD(self):
        self.assertNotEqual(classifyTriangle(3, 6, 5), 'Isosceles', '3,6,5 is not an Isosceles Triangle')

    def testIsoscelesTriangleE(self):
        self.assertNotEqual(classifyTriangle(3, 3, 3), 'Isosceles', '3,3,3 is not an Isosceles Triangle')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4,5,6 is a Scalene Triangle')

    def testScaleneTriangleB(self):
        self.assertNotEqual(classifyTriangle(3, 3, 5), 'Scalene', '3,3,5 is not a scalene triangle')

    def testScaleneTriangleC(self):
        self.assertNotEqual(classifyTriangle(3, 5, 3), 'Scalene', '3,5,3 is not a scalene triangle')

    def testScaleneTriangleD(self):
        self.assertNotEqual(classifyTriangle(5, 3, 3), 'Scalene', '3,4,5 is not a scalene triangle')

    def testScaleneTriangleE(self):
        self.assertNotEqual(classifyTriangle(3, 4, 5), 'Scalene', '3,4,5 is not a scalene triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)

