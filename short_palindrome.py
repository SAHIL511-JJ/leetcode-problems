#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def shortPalindrome(s):
    """
    Count the number of 4-character palindromic subsequences in a string.
    Result modulo 10^9 + 7.
    """
    MOD = 10**9 + 7
    
    # single[i] = count of character i seen so far
    single = [0] * 26
    
    # double[i][j] = count of pairs (i, j) seen so far
    double = [[0] * 26 for _ in range(26)]
    
    # triple[i] = count of valid triples ending with character i
    triple = [0] * 26
    
    result = 0
    
    for char in s:
        idx = ord(char) - ord('a')
        
        # Add triples that can form palindrome with current char
        result = (result + triple[idx]) % MOD
        
        # Update triples: add all doubles that start with current char
        for i in range(26):
            triple[i] = (triple[i] + double[idx][i]) % MOD
        
        # Update doubles: add all singles paired with current char
        for i in range(26):
            double[i][idx] = (double[i][idx] + single[i]) % MOD
        
        # Update singles
        single[idx] += 1
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()
    
    result = shortPalindrome(s)
    
    fptr.write(str(result) + '\n')
    fptr.close()
