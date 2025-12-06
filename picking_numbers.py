#!/usr/bin/env python3
"""
HackerRank: Picking Numbers
https://www.hackerrank.com/challenges/picking-numbers

Given an array of integers, find the longest subarray where the absolute difference
between any two elements is at most 1.
"""

from collections import Counter

def picking_numbers(a):
    """
    Find the longest subarray with absolute difference <= 1.
    
    Args:
        a: list of integers
    
    Returns:
        Length of the longest valid subarray
    """
    count = Counter(a)
    max_length = 0
    
    for num in count:
        # Check pairs (num, num) and (num, num+1)
        current = count[num] + count.get(num + 1, 0)
        max_length = max(max_length, current)
    
    return max_length


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    result = picking_numbers(a)
    print(result)
