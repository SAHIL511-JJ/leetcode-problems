#!/usr/bin/env python3
"""
HackerRank: Birthday Chocolate
https://www.hackerrank.com/challenges/the-birthday-bar

Lily wants to give Ron a piece of chocolate bar. The bar contains n squares.
She wants to give him m contiguous squares where sum equals d (Ron's birth day)
and m is Ron's birth month.
"""

def birthday(s, d, m):
    """
    Count ways to divide chocolate bar.
    
    Args:
        s: list of integers on chocolate squares
        d: Ron's birth day (required sum)
        m: Ron's birth month (required length)
    
    Returns:
        Number of valid segments
    """
    count = 0
    n = len(s)
    
    for i in range(n - m + 1):
        segment_sum = sum(s[i:i + m])
        if segment_sum == d:
            count += 1
    
    return count


if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))
    d, m = map(int, input().split())
    result = birthday(s, d, m)
    print(result)
