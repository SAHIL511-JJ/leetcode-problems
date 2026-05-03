"""
LeetCode #238: Product of Array Except Self
Given an integer array nums, return an array where each element at index i
is the product of all elements in nums except nums[i].
Must run in O(n) time without using division.
"""


def product_except_self(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    result = [1] * n

    # Build prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Build suffix products and multiply
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


if __name__ == "__main__":
    test = [1, 2, 3, 4]
    result = product_except_self(test)
    print(f"Input: {test}")
    print(f"Output: {result}")
