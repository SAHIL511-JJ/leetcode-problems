# Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example 1:
#   Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#   Output: 6
#   Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Example 2:
#   Input: nums = [1]
#   Output: 1
#
# Example 3:
#   Input: nums = [5,4,-1,7,8]
#   Output: 23
#
# Constraints:
#   1 <= nums.length <= 10^5
#   -10^4 <= nums[i] <= 10^4
#
# Approach:
#   Kadane's algorithm:
#   We iterate through the array, maintaining two variables:
#     current_sum: maximum sum ending at the current position
#     max_sum: maximum sum seen so far
#   For each element:
#     current_sum = max(num, current_sum + num)
#     max_sum = max(max_sum, current_sum)
#
#   Time Complexity: O(n)
#   Space Complexity: O(1)

def max_subarray(nums):
    '''
    :type nums: List[int]
    :rtype: int
    '''
    if not nums:
        return 0
    
    current_sum = max_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage:
if __name__ == '__main__':
    test_cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([1], 1),
        ([5,4,-1,7,8], 23),
        ([-1], -1),
        ([-2,-1], -1)
    ]
    
    for nums, expected in test_cases:
        result = max_subarray(nums)
        print(f'Input: nums = {nums}')
        print(f'Expected: {expected}')
        print(f'Got: {result}')
        print(f'{\
PASS\ if result == expected else \FAIL\}')
        print()

