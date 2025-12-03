#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    """
    Find the maximum size of a subset where no two elements sum to a multiple of k.
    """
    # Count remainders when divided by k
    remainder_count = [0] * k
    
    for num in s:
        remainder_count[num % k] += 1
    
    # Start with elements divisible by k (remainder 0) - can only take 1
    result = min(1, remainder_count[0])
    
    # For remainders that pair up to k
    for i in range(1, (k // 2) + 1):
        if i != k - i:
            # Take the larger group of complementary remainders
            result += max(remainder_count[i], remainder_count[k - i])
        else:
            # If k is even and i = k/2, can only take 1
            result += min(1, remainder_count[i])
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    
    s = list(map(int, input().rstrip().split()))
    
    result = nonDivisibleSubset(k, s)
    
    fptr.write(str(result) + '\n')
    fptr.close()
