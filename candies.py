#!/usr/bin/env python3
"""
HackerRank: Candies
https://www.hackerrank.com/challenges/candies

Each student must receive at least one candy.
Students with higher ratings than neighbors must get more candies.
Find minimum candies needed.
"""

def candies(n, arr):
    """
    Find minimum candies to distribute.
    
    Args:
        n: number of students
        arr: list of ratings
    
    Returns:
        Minimum candies needed
    """
    if n == 0:
        return 0
    
    candies_arr = [1] * n
    
    # Left to right pass
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            candies_arr[i] = candies_arr[i-1] + 1
    
    # Right to left pass
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            candies_arr[i] = max(candies_arr[i], candies_arr[i+1] + 1)
    
    return sum(candies_arr)


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    result = candies(n, arr)
    print(result)
