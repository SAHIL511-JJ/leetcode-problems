class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    height1 = [1,8,6,2,5,4,8,3,7]
    result1 = solution.maxArea(height1)
    print(f"Input: {height1} -> Output: {result1}")
    
    # Test case 2
    height2 = [1,1]
    result2 = solution.maxArea(height2)
    print(f"Input: {height2} -> Output: {result2}")
    
    # Test case 3
    height3 = [4,3,2,1,4]
    result3 = solution.maxArea(height3)
    print(f"Input: {height3} -> Output: {result3}")