class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    result1 = solution.search(nums1, target1)
    print(f"Input: nums={nums1}, target={target1} -> Output: {result1}")
    
    # Test case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    result2 = solution.search(nums2, target2)
    print(f"Input: nums={nums2}, target={target2} -> Output: {result2}")
    
    # Test case 3
    nums3 = [5]
    target3 = 5
    result3 = solution.search(nums3, target3)
    print(f"Input: nums={nums3}, target={target3} -> Output: {result3}")