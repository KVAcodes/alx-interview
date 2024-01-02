#!/usr/bin/python3
"""Solution to the Minimum Operation Interview Question."""


def findHF(n):
    """Finds the highest factor of a number.
    """
    highestFactor = 1
    num = 2
    while num <= n / 2:
        if n % num == 0:
            highestFactor = num
        num += 1
    return highestFactor


def minOperations(n):
    """This method calculates the fewest number of operations needed to
    result in exactly n H characters.
    """
    ops = 0
    if n <= 1:
        return ops
    highestFactor = findHF(n)
    if highestFactor == 1:
        return n
    ret = minOperations(highestFactor)
    return int(ret + (n / highestFactor))
