#!/usr/bin/env python3
"""
HackerRank: Cats and a Mouse
https://www.hackerrank.com/challenges/cats-and-a-mouse

Two cats and a mouse are at various positions on a line. Cat A is at position x,
Cat B is at position y, and the mouse is at position z.

Determine which cat will reach the mouse first, assuming they start at the same time
and move at the same speed.
"""

def cat_and_mouse(x, y, z):
    """
    Determine which cat catches the mouse first.
    
    Args:
        x: position of Cat A
        y: position of Cat B
        z: position of Mouse C
    
    Returns:
        'Cat A', 'Cat B', or 'Mouse C' (if both cats are equidistant)
    """
    dist_a = abs(x - z)
    dist_b = abs(y - z)
    
    if dist_a < dist_b:
        return 'Cat A'
    elif dist_b < dist_a:
        return 'Cat B'
    else:
        return 'Mouse C'


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        x, y, z = map(int, input().split())
        result = cat_and_mouse(x, y, z)
        print(result)
