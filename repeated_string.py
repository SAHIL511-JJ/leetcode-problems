#!/usr/bin/env python3
"""
HackerRank: Repeated String
https://www.hackerrank.com/challenges/repeated-string

Lilah has a string s of lowercase letters that she repeated infinitely.
Given n, find how many 'a' characters are in the first n characters.
"""

def repeated_string(s, n):
    """
    Count 'a' in first n chars of infinitely repeated string.
    
    Args:
        s: the string to repeat
        n: number of characters to consider
    
    Returns:
        Count of 'a' characters
    """
    # Count 'a' in one copy of s
    a_count_in_s = s.count('a')
    
    # How many complete copies of s fit in n?
    complete_copies = n // len(s)
    
    # Remaining characters after complete copies
    remainder = n % len(s)
    
    # Count 'a' in the remainder
    a_count_in_remainder = s[:remainder].count('a')
    
    return (complete_copies * a_count_in_s) + a_count_in_remainder


if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeated_string(s, n)
    print(result)
