#!/usr/bin/env python3
"""
HackerRank: Diagonal Difference
https://www.hackerrank.com/challenges/diagonal-difference

Given a square matrix, calculate the absolute difference
between the sums of its diagonals.
"""

def diagonal_difference(arr):
    """
    Calculate absolute difference between diagonal sums.
    
    Args:
        arr: 2D square matrix
    
    Returns:
        Absolute difference between diagonal sums
    """
    n = len(arr)
    primary_diagonal = sum(arr[i][i] for i in range(n))
    secondary_diagonal = sum(arr[i][n - 1 - i] for i in range(n))
    
    return abs(primary_diagonal - secondary_diagonal)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
    result = diagonal_difference(arr)
    print(result)
