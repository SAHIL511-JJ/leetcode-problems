#!/usr/bin/env python3
"""
HackerRank: A Very Big Sum
https://www.hackerrank.com/challenges/a-very-big-sum

Calculate and print the sum of elements in an array,
keeping in mind that some of those integers may be quite large.
"""

def a_very_big_sum(ar):
    """
    Calculate sum of potentially large integers.
    
    Args:
        ar: list of integers (can be very large)
    
    Returns:
        Sum of all elements
    """
    return sum(ar)


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().split()))
    result = a_very_big_sum(ar)
    print(result)
