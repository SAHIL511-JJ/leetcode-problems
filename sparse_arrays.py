#!/usr/bin/env python3
"""
HackerRank: Sparse Arrays
https://www.hackerrank.com/challenges/sparse-arrays

Given a collection of strings and queries, count occurrences
of each query string in the collection.
"""

from collections import Counter

def matching_strings(strings, queries):
    """
    Count occurrences of each query in strings.
    
    Args:
        strings: list of input strings
        queries: list of query strings
    
    Returns:
        List of counts for each query
    """
    count = Counter(strings)
    return [count[q] for q in queries]


if __name__ == '__main__':
    n = int(input())
    strings = [input() for _ in range(n)]
    q = int(input())
    queries = [input() for _ in range(q)]
    result = matching_strings(strings, queries)
    print('\n'.join(map(str, result)))
