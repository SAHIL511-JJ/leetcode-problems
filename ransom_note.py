#!/usr/bin/env python3
"""
HackerRank: Hash Tables - Ransom Note
https://www.hackerrank.com/challenges/ctci-ransom-note

Determine if a ransom note can be constructed from words in a magazine.
"""

from collections import Counter

def check_magazine(magazine, note):
    """
    Check if ransom note can be made from magazine words.
    
    Args:
        magazine: list of words in magazine
        note: list of words needed for ransom note
    
    Returns:
        'Yes' if possible, 'No' otherwise
    """
    mag_count = Counter(magazine)
    note_count = Counter(note)
    
    for word, count in note_count.items():
        if mag_count[word] < count:
            return 'No'
    return 'Yes'


if __name__ == '__main__':
    m, n = map(int, input().split())
    magazine = input().split()
    note = input().split()
    result = check_magazine(magazine, note)
    print(result)
