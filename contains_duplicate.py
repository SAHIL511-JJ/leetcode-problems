# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
# Example 1:
#   Input: nums = [1,2,3,1]
#   Output: true
#
# Example 2:
#   Input: nums = [1,2,3,4]
#   Output: false
#
# Example 3:
#   Input: nums = [1,1,1,3,3,4,3,2,4,2]
#   Output: true
#
# Constraints:
#   1 <= nums.length <= 10^5
#   -10^9 <= nums[i] <= 10^9
#
# Approach:
#   Use a hash set to track seen numbers.
#   Iterate through the array, for each number:
#     If it's already in the set, return true (duplicate found)
#     Otherwise, add it to the set
#   If we finish iteration without finding duplicates, return false.
#
#   Time Complexity: O(n) where n is the length of nums
#   Space Complexity: O(n) for the hash set

def contains_duplicate(nums):
    '''
    :type nums: List[int]
    :rtype: bool
    '''
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example usage:
if __name__ == '__main__':
    test_cases = [
        ([1,2,3,1], True),
        ([1,2,3,4], False),
        ([1,1,1,3,3,4,3,2,4,2], True),
        ([], False),
        ([1], False)
    ]
    
    for nums, expected in test_cases:
        result = contains_duplicate(nums)
        print(f'Input: nums = {nums}')
        print(f'Expected: {expected}')
        print(f'Got: {result}')
        print(f'{\
PASS\ if result == expected else \FAIL\}')
        print()

