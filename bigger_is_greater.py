#!/bin/python3

import os

def biggerIsGreater(w):
    """
    Find the lexicographically next greater permutation of a string.
    
    Args:
        w: Input string
    
    Returns:
        Next greater permutation or "no answer"
    """
    chars = list(w)
    n = len(chars)
    
    # Step 1: Find the rightmost character which is smaller than its next character
    i = n - 2
    while i >= 0 and chars[i] >= chars[i + 1]:
        i -= 1
    
    # If no such character is found, no greater permutation exists
    if i == -1:
        return "no answer"
    
    # Step 2: Find the smallest character on right side of i that is greater than chars[i]
    j = n - 1
    while chars[j] <= chars[i]:
        j -= 1
    
    # Step 3: Swap characters at i and j
    chars[i], chars[j] = chars[j], chars[i]
    
    # Step 4: Reverse the substring after position i
    chars[i + 1:] = reversed(chars[i + 1:])
    
    return ''.join(chars)

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')
    T = int(input().strip())
    for _ in range(T):
        w = input()
        result = biggerIsGreater(w)
        fptr.write(result + '\n')
    fptr.close()
