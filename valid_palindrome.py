class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the filtered string is equal to its reverse
        return filtered == filtered[::-1]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "A man, a plan, a canal: Panama"
    result1 = solution.isPalindrome(s1)
    print(f"Input: \"{s1}\" -> Output: {result1}")
    
    # Test case 2
    s2 = "race a car"
    result2 = solution.isPalindrome(s2)
    print(f"Input: \"{s2}\" -> Output: {result2}")
    
    # Test case 3
    s3 = ""
    result3 = solution.isPalindrome(s3)
    print(f"Input: \"{s3}\" -> Output: {result3}")