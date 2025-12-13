#!/usr/bin/env python3
"""
HackerRank: Between Two Sets
https://www.hackerrank.com/challenges/between-two-sets

Find integers that are factors of all elements in array b and 
have all elements of array a as factors.
"""

from math import gcd
from functools import reduce

def lcm(a, b):
    """Calculate least common multiple."""
    return a * b // gcd(a, b)

def get_total_x(a, b):
    """
    Count integers between two sets.
    
    Args:
        a: first array (factors)
        b: second array (multiples)
    
    Returns:
        Count of valid integers
    """
    # LCM of all elements in a
    lcm_a = reduce(lcm, a)
    
    # GCD of all elements in b
    gcd_b = reduce(gcd, b)
    
    # Count multiples of lcm_a that divide gcd_b
    count = 0
    multiple = lcm_a
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            count += 1
        multiple += lcm_a
    
    return count


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    total = get_total_x(a, b)
    print(total)
