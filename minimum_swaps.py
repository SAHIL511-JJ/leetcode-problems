#!/usr/bin/env python3
"""
HackerRank: Minimum Swaps 2
https://www.hackerrank.com/challenges/minimum-swaps-2

Given an unordered array of consecutive integers [1, 2, 3, ..., n],
find the minimum number of swaps to sort the array.
"""

def minimum_swaps(arr):
    """
    Find minimum swaps to sort array.
    
    Args:
        arr: unordered array of consecutive integers
    
    Returns:
        Minimum number of swaps
    """
    n = len(arr)
    swaps = 0
    
    # Create position mapping
    pos = {val: idx for idx, val in enumerate(arr)}
    
    for i in range(n):
        correct_val = i + 1
        
        if arr[i] != correct_val:
            # Swap current element with the element at its correct position
            current_val = arr[i]
            correct_pos = pos[correct_val]
            
            # Swap in array
            arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
            
            # Update position mapping
            pos[current_val] = correct_pos
            pos[correct_val] = i
            
            swaps += 1
    
    return swaps


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = minimum_swaps(arr)
    print(result)
