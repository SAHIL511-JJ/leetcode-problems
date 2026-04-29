class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Two pointers approach
        # slow pointer for the position to place next non-zero element
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        
        # Fill the remaining positions with zeros
        for i in range(slow, len(nums)):
            nums[i] = 0

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [0,1,0,3,12]
    solution.moveZeroes(nums1)
    print(f"Input: [0,1,0,3,12] -> Output: {nums1}")
    
    # Test case 2
    nums2 = [0]
    solution.moveZeroes(nums2)
    print(f"Input: [0] -> Output: {nums2}")