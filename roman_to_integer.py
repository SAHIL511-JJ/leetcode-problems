class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate from right to left
        for char in reversed(s):
            value = roman_values[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "III"
    result1 = solution.romanToInt(s1)
    print(f"Input: \"{s1}\" -> Output: {result1}")
    
    # Test case 2
    s2 = "LVIII"
    result2 = solution.romanToInt(s2)
    print(f"Input: \"{s2}\" -> Output: {result2}")
    
    # Test case 3
    s3 = "MCMXCIV"
    result3 = solution.romanToInt(s3)
    print(f"Input: \"{s3}\" -> Output: {result3}")