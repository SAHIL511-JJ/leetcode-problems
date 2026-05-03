"""
LeetCode #242: Valid Anagram
Given two strings, return true if the second is an anagram of the first.
"""


def is_anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True


def is_anagram_sort(s, t):
    """Alternative: sort both strings and compare."""
    return sorted(s) == sorted(t)


def is_anagram_counter(s, t):
    """Using Python's Counter for a clean one-liner."""
    from collections import Counter

    return Counter(s) == Counter(t)


if __name__ == "__main__":
    print(f"'anagram' vs 'nagaram': {is_anagram('anagram', 'nagaram')}")
    print(f"'rat' vs 'car': {is_anagram('rat', 'car')}")
    print(f"'silent' vs 'listen': {is_anagram('silent', 'listen')}")
