#!/usr/bin/env python3
"""
HackerRank: Solve Me First
https://www.hackerrank.com/challenges/solve-me-first

Complete the function solveMeFirst to compute the sum of two integers.
"""

def solve_me_first(a, b):
    """
    Compute sum of two integers.
    
    Args:
        a: first integer
        b: second integer
    
    Returns:
        Sum of a and b
    """
    return a + b


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    result = solve_me_first(a, b)
    print(result)
