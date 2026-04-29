class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # 1-indexed
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(numbers1, target1)
    print(f"Input: numbers={numbers1}, target={target1} -> Output: {result1}")
    
    # Test case 2
    numbers2 = [2, 3, 4]
    target2 = 6
    result2 = solution.twoSum(numbers2, target2)
    print(f"Input: numbers={numbers2}, target={target2} -> Output: {result2}")
    
    # Test case 3
    numbers3 = [-1, 0]
    target3 = -1
    result3 = solution.twoSum(numbers3, target3)
    print(f"Input: numbers={numbers3}, target={target3} -> Output: {result3}")