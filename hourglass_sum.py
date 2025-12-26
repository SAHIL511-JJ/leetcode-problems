#!/usr/bin/env python3
"""
HackerRank: 2D Array - DS (Hourglass Sum)
https://www.hackerrank.com/challenges/2d-array

Given a 6x6 2D array, calculate the hourglass sum for every hourglass.
Return the maximum hourglass sum.

An hourglass pattern:
a b c
  d
e f g
"""

def hourglass_sum(arr):
    """
    Find maximum hourglass sum in 6x6 array.
    
    Args:
        arr: 6x6 2D array
    
    Returns:
        Maximum hourglass sum
    """
    max_sum = float('-inf')
    
    # Iterate through all possible hourglass positions
    for i in range(4):
        for j in range(4):
            # Calculate hourglass sum
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            current_sum = top + middle + bottom
            max_sum = max(max_sum, current_sum)
    
    return max_sum


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        row = list(map(int, input().split()))
        arr.append(row)
    result = hourglass_sum(arr)
    print(result)
