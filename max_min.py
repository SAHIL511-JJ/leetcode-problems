#!/usr/bin/env python3
"""
HackerRank: Max Min
https://www.hackerrank.com/challenges/angry-children

Given a list of integers, find the minimum unfairness.
Pick k integers where unfairness = max(picked) - min(picked).
"""

def max_min(k, arr):
    """
    Find minimum unfairness when picking k elements.
    
    Args:
        k: number of elements to pick
        arr: list of integers
    
    Returns:
        Minimum unfairness
    """
    arr.sort()
    min_unfairness = float('inf')
    
    for i in range(len(arr) - k + 1):
        unfairness = arr[i + k - 1] - arr[i]
        min_unfairness = min(min_unfairness, unfairness)
    
    return min_unfairness


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    arr = [int(input()) for _ in range(n)]
    result = max_min(k, arr)
    print(result)
