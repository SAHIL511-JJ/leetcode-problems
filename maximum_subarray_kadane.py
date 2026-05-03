"""
LeetCode #53: Maximum Subarray (Kadane's Algorithm)
Given an integer array, find the contiguous subarray with the largest sum.
"""


def max_subarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_with_indices(nums):
    """Returns the max sum along with start and end indices."""
    current_sum = nums[0]
    max_sum = nums[0]
    start = 0
    max_start = 0
    max_end = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            max_start = start
            max_end = i

    return max_sum, max_start, max_end


if __name__ == "__main__":
    test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray(test)
    print(f"Maximum Subarray Sum: {result}")
