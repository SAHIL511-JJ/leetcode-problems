#!/usr/bin/env python3
"""
HackerRank: Staircase
https://www.hackerrank.com/challenges/staircase

Print a right-aligned staircase of height n using # symbols.
"""

def staircase(n):
    """
    Print a staircase of size n.
    
    Args:
        n: height of the staircase
    """
    for i in range(1, n + 1):
        # Print spaces followed by hashes
        spaces = ' ' * (n - i)
        hashes = '#' * i
        print(spaces + hashes)


if __name__ == '__main__':
    n = int(input())
    staircase(n)
