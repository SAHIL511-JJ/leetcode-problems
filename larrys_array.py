#!/bin/python3

import os

def larrysArray(A):
    """
    Determine if array can be sorted using rotation operation on 3 consecutive elements.
    Key insight: Count inversions. If even, array can be sorted; if odd, it cannot.
    
    Args:
        A: Array to check
    
    Returns:
        "YES" if sortable, "NO" otherwise
    """
    # Count inversions
    inversions = 0
    n = len(A)
    
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                inversions += 1
    
    # If inversions is even, array can be sorted
    return "YES" if inversions % 2 == 0 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        A = list(map(int, input().rstrip().split()))
        result = larrysArray(A)
        fptr.write(result + '\n')
    fptr.close()
