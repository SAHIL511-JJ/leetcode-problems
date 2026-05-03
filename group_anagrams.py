"""
LeetCode #49: Group Anagrams
Given an array of strings, group the anagrams together.
Two strings are anagrams if they contain the same characters with the same frequency.
"""


def group_anagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagram_map = {}

    for s in strs:
        key = tuple(sorted(s))
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(s)

    return list(anagram_map.values())


if __name__ == "__main__":
    test = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(test)
    print(f"Group Anagrams: {result}")
