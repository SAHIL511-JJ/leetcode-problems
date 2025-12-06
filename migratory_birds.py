#!/usr/bin/env python3
"""
HackerRank: Migratory Birds
https://www.hackerrank.com/challenges/migratory-birds

Given an array of bird sightings (bird type IDs), determine which type of bird
is most commonly sighted. If two or more types are equally common, return the
type with the smallest ID number.
"""

from collections import Counter

def migratory_birds(arr):
    """
    Find the most common bird type.
    
    Args:
        arr: list of bird type IDs
    
    Returns:
        The most common bird type ID (smallest ID if tie)
    """
    count = Counter(arr)
    max_sightings = max(count.values())
    
    # Find smallest ID with max sightings
    most_common = min(bird for bird, cnt in count.items() if cnt == max_sightings)
    
    return most_common


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = migratory_birds(arr)
    print(result)
