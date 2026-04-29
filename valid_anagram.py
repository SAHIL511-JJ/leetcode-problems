class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        # Count frequency of characters in s
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Subtract frequency for characters in t
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
        
        return True

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "anagram"
    t1 = "nagaram"
    result1 = solution.isAnagram(s1, t1)
    print(f"Input: s='{s1}', t='{t1}' -> Output: {result1}")
    
    # Test case 2
    s2 = "rat"
    t2 = "car"
    result2 = solution.isAnagram(s2, t2)
    print(f"Input: s='{s2}', t='{t2}' -> Output: {result2}")
    
    # Test case 3
    s3 = ""
    t3 = ""
    result3 = solution.isAnagram(s3, t3)
    print(f"Input: s='{s3}', t='{t3}' -> Output: {result3}")