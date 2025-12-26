#!/usr/bin/env python3
"""
HackerRank: Sales by Match (Sock Merchant variant)
https://www.hackerrank.com/challenges/sock-merchant

There is a large pile of socks that must be paired by color.
Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.
"""

from collections import Counter

def sales_by_match(n, ar):
    """
    Count pairs of matching socks.
    
    Args:
        n: number of socks
        ar: list of sock colors
    
    Returns:
        Number of pairs
    """
    color_counts = Counter(ar)
    pairs = sum(count // 2 for count in color_counts.values())
    return pairs


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().split()))
    result = sales_by_match(n, ar)
    print(result)
