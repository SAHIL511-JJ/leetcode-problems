#!/bin/python3

import os

def absolutePermutation(n, k):
    """
    Find the lexicographically smallest absolute permutation.
    Absolute permutation: |pos[i] - i| = k for all i
    
    Args:
        n: Size of permutation
        k: Absolute difference required
    
    Returns:
        Lexicographically smallest permutation or [-1] if impossible
    """
    if k == 0:
        return list(range(1, n + 1))
    
    # Check if solution is possible
    if n % (2 * k) != 0:
        return [-1]
    
    result = [0] * n
    
    # Swap elements in blocks of size 2k
    for i in range(n):
        # Determine which block of 2k we're in
        block = (i // k) % 2
        
        if block == 0:
            # First half of block: add k
            result[i] = i + 1 + k
        else:
            # Second half of block: subtract k
            result[i] = i + 1 - k
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')
    t = int(input().strip())
    for _ in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        result = absolutePermutation(n, k)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()
