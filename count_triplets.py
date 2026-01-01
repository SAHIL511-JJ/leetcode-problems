#!/usr/bin/env python3
"""
HackerRank: Count Triplets
https://www.hackerrank.com/challenges/count-triplets-1

Count triplets (i, j, k) where i < j < k and elements form geometric progression.
"""

from collections import defaultdict

def count_triplets(arr, r):
    """
    Count geometric progression triplets.
    
    Args:
        arr: list of integers
        r: common ratio
    
    Returns:
        Number of valid triplets
    """
    left = defaultdict(int)   # Count of elements to the left
    right = defaultdict(int)  # Count of elements to the right
    
    # Initialize right counter
    for num in arr:
        right[num] += 1
    
    count = 0
    for num in arr:
        right[num] -= 1
        
        if num % r == 0:
            left_val = num // r
            right_val = num * r
            count += left[left_val] * right[right_val]
        
        left[num] += 1
    
    return count


if __name__ == '__main__':
    n, r = map(int, input().split())
    arr = list(map(int, input().split()))
    result = count_triplets(arr, r)
    print(result)
