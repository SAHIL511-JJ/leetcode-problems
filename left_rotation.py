#!/usr/bin/env python3
"""
HackerRank: Left Rotation
https://www.hackerrank.com/challenges/ctci-array-left-rotation

A left rotation operation on an array shifts each element to the left by one.
Given an array and number of rotations, return the updated array.
"""

def left_rotation(a, d):
    """
    Perform d left rotations on array.
    
    Args:
        a: list of integers
        d: number of left rotations
    
    Returns:
        Rotated array
    """
    n = len(a)
    d = d % n  # Handle rotations greater than array length
    return a[d:] + a[:d]


if __name__ == '__main__':
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    result = left_rotation(a, d)
    print(' '.join(map(str, result)))
