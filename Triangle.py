# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def check_input(f_side, s_side, t_side):
    """ Function to check input """

    valid = True
    if not(isinstance(f_side, int) and isinstance(s_side, int) and isinstance(t_side, int)):
        # return 'InvalidInput'
        valid = False

    # require that the input values be >= 0 and <= 200
    elif f_side > 200 or s_side > 200 or t_side > 200:
        # return 'InvalidInput'
        valid = False

    elif f_side <= 0 or s_side <= 0 or t_side <= 0:
        # return 'InvalidInput'
        valid = False

    return valid


def classify_triangle(f_side, s_side, t_side):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      BEWARE: there may be a bug or two in this code
    """
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not check_input(f_side, s_side, t_side):
        return "InvalidInput"

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    # if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
    if ((f_side + s_side) < t_side) or ((s_side + t_side) < f_side) or ((f_side + t_side) < s_side):
        return "NotATriangle"

    # now we know that we have a valid triangle
    f_side, s_side, t_side = sorted([f_side, s_side, t_side])
    if f_side == s_side and s_side == t_side:
        return 'Equilateral'

    elif ((f_side * f_side) + (s_side * s_side)) == (t_side * t_side):
        return 'Right'

    elif (f_side == s_side and s_side != t_side) or (s_side == t_side and t_side != f_side) or (f_side == t_side and s_side != t_side):
        return 'Isosceles'

    else:
        return 'Scalene'
