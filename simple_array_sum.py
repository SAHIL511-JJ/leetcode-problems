#!/usr/bin/env python3
"""
HackerRank: Simple Array Sum
https://www.hackerrank.com/challenges/simple-array-sum

Given an array of integers, find the sum of its elements.
"""

def simple_array_sum(ar):
    """
    Calculate sum of array elements.
    
    Args:
        ar: list of integers
    
    Returns:
        Sum of all elements
    """
    return sum(ar)


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().split()))
    result = simple_array_sum(ar)
    print(result)
