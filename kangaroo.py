#!/usr/bin/env python3
"""
HackerRank: Kangaroo
https://www.hackerrank.com/challenges/kangaroo

Two kangaroos start at positions x1, x2 and jump v1, v2 meters per jump.
Determine if they land at the same location at the same time.
"""

def kangaroo(x1, v1, x2, v2):
    """
    Determine if kangaroos meet at same location.
    
    Args:
        x1: starting position of kangaroo 1
        v1: jump distance of kangaroo 1
        x2: starting position of kangaroo 2
        v2: jump distance of kangaroo 2
    
    Returns:
        'YES' if they meet, 'NO' otherwise
    """
    # If same speed, they only meet if starting at same position
    if v1 == v2:
        return 'YES' if x1 == x2 else 'NO'
    
    # Check if they can meet: (x2 - x1) / (v1 - v2) must be positive integer
    # Kangaroo 1 must be behind but faster, or ahead but slower
    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    x1, v1, x2, v2 = map(int, input().split())
    result = kangaroo(x1, v1, x2, v2)
    print(result)
