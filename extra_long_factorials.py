#!/bin/python3

import math

def extraLongFactorials(n):
    """
    Calculate and print factorial of very large numbers.
    Python handles arbitrary precision integers natively.
    
    Args:
        n: Number to calculate factorial for
    """
    result = math.factorial(n)
    print(result)

if __name__ == '__main__':
    n = int(input().strip())
    extraLongFactorials(n)
