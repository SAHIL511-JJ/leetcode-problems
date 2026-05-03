"""
LeetCode #136: Single Number
Given a non-empty array where every element appears twice except for one,
find that single one. Must run in O(n) time and O(1) space.
Uses XOR property: a ^ a = 0 and a ^ 0 = a
"""


def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 0
    for num in nums:
        result ^= num
    return result


def single_number_2(nums):
    """
    Variant: Every element appears three times except one.
    Find the single one.
    """
    ones, twos = 0, 0

    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones


if __name__ == "__main__":
    test = [4, 1, 2, 1, 2]
    result = single_number(test)
    print(f"Single Number: {result}")
