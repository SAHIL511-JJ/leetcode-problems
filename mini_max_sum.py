#!/usr/bin/env python3
"""
HackerRank: Mini-Max Sum
https://www.hackerrank.com/challenges/mini-max-sum

Given five positive integers, find the minimum and maximum values
that can be calculated by summing exactly four of the five integers.
"""

def mini_max_sum(arr):
    """
    Find min and max sum of 4 out of 5 integers.
    
    Args:
        arr: list of 5 integers
    
    Returns:
        Tuple of (min_sum, max_sum)
    """
    total = sum(arr)
    min_sum = total - max(arr)
    max_sum = total - min(arr)
    return min_sum, max_sum


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    min_sum, max_sum = mini_max_sum(arr)
    print(min_sum, max_sum)
