class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Two pointers approach
        # i for the position to place next non-val element
        # j for scanning through the array
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print(f"Input: nums={nums1}, val={val1} -> Output: {k1}, nums={nums1[:k1]}")
    
    # Test case 2
    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print(f"Input: nums={nums2}, val={val2} -> Output: {k2}, nums={nums2[:k2]}")
    
    # Test case 3
    nums3 = [3,3]
    val3 = 3
    k3 = solution.removeElement(nums3, val3)
    print(f"Input: nums={nums3}, val={val3} -> Output: {k3}, nums={nums3[:k3]}")