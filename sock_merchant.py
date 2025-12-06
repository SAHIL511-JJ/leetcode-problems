#!/usr/bin/env python3
"""
HackerRank: Sock Merchant
https://www.hackerrank.com/challenges/sock-merchant

There is a large pile of socks that must be paired by color.
Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.
"""

from collections import Counter

def sock_merchant(n, ar):
    """
    Count pairs of socks with matching colors.
    
    Args:
        n: number of socks
        ar: array of sock colors
    
    Returns:
        Number of matching pairs
    """
    color_count = Counter(ar)
    pairs = 0
    
    for color, count in color_count.items():
        pairs += count // 2
    
    return pairs


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().split()))
    result = sock_merchant(n, ar)
    print(result)
