# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#   Input: nums = [2,7,11,15], target = 9
#   Output: [0,1]
#   Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
#   Input: nums = [3,2,4], target = 6
#   Output: [1,2]
#
# Example 3:
#   Input: nums = [3,3], target = 6
#   Output: [0,1]
#
# Constraints:
#   2 <= nums.length <= 10^4
#   -10^9 <= nums[i] <= 10^9
#   -10^9 <= target <= 10^9
#   Only one valid answer exists.
#
# Approach:
#   We can use a hash map to store the numbers we've seen so far along with their indices.
#   For each number, we calculate its complement (target - current number).
#   If the complement exists in our hash map, we've found our solution.
#   Otherwise, we add the current number and its index to the hash map.
#
#   Time Complexity: O(n) where n is the length of the array
#   Space Complexity: O(n) for the hash map

def two_sum(nums, target):
    '''
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    '''
    num_map = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    # According to constraints, we should always find a solution
    return []

# Example usage:
if __name__ == '__main__':
    # Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print('Example 1:')
    print('  Input: nums =', nums1, ', target =', target1)
    print('  Output:', result1)
    print('  Explanation: nums[{}] + nums[{}] = {} + {} = {}'.format(result1[0], result1[1], nums1[result1[0]], nums1[result1[1]], target1))
    print()
    
    # Example 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print('Example 2:')
    print('  Input: nums =', nums2, ', target =', target2)
    print('  Output:', result2)
    print('  Explanation: nums[{}] + nums[{}] = {} + {} = {}'.format(result2[0], result2[1], nums2[result2[0]], nums2[result2[1]], target2))
    print()
    
    # Example 3
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    print('Example 3:')
    print('  Input: nums =', nums3, ', target =', target3)
    print('  Output:', result3)
    print('  Explanation: nums[{}] + nums[{}] = {} + {} = {}'.format(result3[0], result3[1], nums3[result3[0]], nums3[result3[1]], target3))

