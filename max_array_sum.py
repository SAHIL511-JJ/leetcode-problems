#!/usr/bin/env python3
"""
HackerRank: Max Array Sum
https://www.hackerrank.com/challenges/max-array-sum

Find maximum sum of non-adjacent elements in array.
"""

def max_subset_sum(arr):
    """
    Find max sum of non-adjacent elements using DP.
    
    Args:
        arr: list of integers
    
    Returns:
        Maximum sum
    """
    if not arr:
        return 0
    if len(arr) == 1:
        return max(0, arr[0])
    
    # dp[i] = max sum using elements up to index i
    prev2 = max(0, arr[0])
    prev1 = max(prev2, arr[1])
    
    for i in range(2, len(arr)):
        current = max(prev1, prev2 + arr[i], arr[i])
        prev2 = prev1
        prev1 = current
    
    return prev1


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = max_subset_sum(arr)
    print(result)
