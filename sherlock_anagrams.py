#!/usr/bin/env python3
"""
HackerRank: Sherlock and Anagrams
https://www.hackerrank.com/challenges/sherlock-and-anagrams

Find the number of pairs of substrings that are anagrams of each other.
"""

from collections import Counter

def sherlock_and_anagrams(s):
    """
    Count anagram pairs in string.
    
    Args:
        s: input string
    
    Returns:
        Number of anagram pairs
    """
    anagram_count = Counter()
    
    # Generate all substrings and their sorted form
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            sorted_sub = ''.join(sorted(substring))
            anagram_count[sorted_sub] += 1
    
    # Count pairs: n choose 2 = n * (n-1) / 2
    pairs = 0
    for count in anagram_count.values():
        if count > 1:
            pairs += count * (count - 1) // 2
    
    return pairs


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input()
        result = sherlock_and_anagrams(s)
        print(result)
