#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    """
    Determine if array can be sorted by swapping exactly 2 elements or 
    reversing a subsegment.
    """
    n = len(arr)
    sorted_arr = sorted(arr)
    
    if arr == sorted_arr:
        print("yes")
        return
    
    # Find positions where array differs from sorted version
    diff_positions = []
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            diff_positions.append(i)
    
    # Check if can be fixed by swapping 2 elements
    if len(diff_positions) == 2:
        i, j = diff_positions
        if arr[i] == sorted_arr[j] and arr[j] == sorted_arr[i]:
            print(f"yes")
            print(f"swap {i + 1} {j + 1}")
            return
    
    # Check if can be fixed by reversing a segment
    if len(diff_positions) > 2:
        left = diff_positions[0]
        right = diff_positions[-1]
        
        # Reverse the segment and check
        test_arr = arr[:]
        test_arr[left:right + 1] = reversed(test_arr[left:right + 1])
        
        if test_arr == sorted_arr:
            print("yes")
            print(f"reverse {left + 1} {right + 1}")
            return
    
    print("no")

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    almostSorted(arr)
