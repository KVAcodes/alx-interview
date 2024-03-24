#!/usr/bin/python3
""" This module contains the solution to the pascal triangle
interview question.
"""


def pascal_triangle(n):
    """This function returns a list of lists of integers representing
    the Pascal's triangle of n
    """
    if n <= 0:
        return []
    triangle = [[1]]
    if n == 1:
        return triangle

    for index in range(n - 1):
        back = 0
        newList = []
        for num in triangle[index]:
            front = num
            newList.append(front + back)
            back = front
        newList.append(1)
        triangle.append(newList)

    return triangle
