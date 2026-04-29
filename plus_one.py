class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        # Start from the last digit
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If all digits were 9
        return [1] + digits

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    digits1 = [1, 2, 3]
    result1 = solution.plusOne(digits1.copy())
    print(f"Input: {digits1} -> Output: {result1}")
    
    # Test case 2
    digits2 = [4, 3, 2, 1]
    result2 = solution.plusOne(digits2.copy())
    print(f"Input: {digits2} -> Output: {result2}")
    
    # Test case 3
    digits3 = [9]
    result3 = solution.plusOne(digits3.copy())
    print(f"Input: {digits3} -> Output: {result3}")
    
    # Test case 4
    digits4 = [9, 9, 9]
    result4 = solution.plusOne(digits4.copy())
    print(f"Input: {digits4} -> Output: {result4}")