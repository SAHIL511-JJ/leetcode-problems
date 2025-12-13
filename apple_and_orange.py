#!/usr/bin/env python3
"""
HackerRank: Apple and Orange
https://www.hackerrank.com/challenges/apple-and-orange

Sam's house is between points s and t. Apple tree at point a, orange tree at point b.
Count apples and oranges that land on Sam's house.
"""

def count_apples_and_oranges(s, t, a, b, apples, oranges):
    """
    Count fruits landing on the house.
    
    Args:
        s: start of house
        t: end of house
        a: position of apple tree
        b: position of orange tree
        apples: list of apple distances
        oranges: list of orange distances
    
    Returns:
        Tuple of (apple_count, orange_count)
    """
    apple_count = sum(1 for d in apples if s <= a + d <= t)
    orange_count = sum(1 for d in oranges if s <= b + d <= t)
    
    return apple_count, orange_count


if __name__ == '__main__':
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())
    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))
    
    apple_count, orange_count = count_apples_and_oranges(s, t, a, b, apples, oranges)
    print(apple_count)
    print(orange_count)
