#!/usr/bin/env python3
"""
HackerRank: Two Strings
https://www.hackerrank.com/challenges/two-strings

Given two strings, determine if they share a common substring.
"""

def two_strings(s1, s2):
    """
    Check if two strings share any common substring.
    
    Args:
        s1: first string
        s2: second string
    
    Returns:
        'YES' if common substring exists, 'NO' otherwise
    """
    # Two strings share a substring if they share any character
    set1 = set(s1)
    set2 = set(s2)
    
    if set1 & set2:  # Intersection
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s1 = input()
        s2 = input()
        result = two_strings(s1, s2)
        print(result)
