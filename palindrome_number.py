# Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# Example 1:
#   Input: x = 121
#   Output: true
#   Explanation: 121 reads as 121 from left to right and from right to left.
#
# Example 2:
#   Input: x = -121
#   Output: false
#   Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
# Example 3:
#   Input: x = 10
#   Output: false
#   Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
# Constraints:
#   -2^31 <= x <= 2^31 - 1
#
# Follow up: Could you solve it without converting the integer to a string?
#
# Approach 1 (String conversion):
#   Convert to string and check if string equals its reverse.
#   Simple but uses extra space.
#
# Approach 2 (Mathematical):
#   Reverse the integer and compare with original.
#   Need to handle overflow? Actually if we reverse the whole number, it might overflow but we can reverse half of the number.
#   However, for simplicity we can use string method since constraints are fine.
#
#   We'll implement both for demonstration.

def is_palindrome_str(x):
    '''
    :type x: int
    :rtype: bool
    '''
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]

def is_palindrome(x):
    '''
    :type x: int
    :rtype: bool
    '''
    # Negative numbers are not palindrome
    if x < 0:
        return False
    
    # If the number ends with 0 but is not 0 itself, it cannot be palindrome
    # because leading zeros are not allowed.
    if x % 10 == 0 and x != 0:
        return False
    
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # When the length is odd, we can get rid of the middle digit by reversed_half // 10
    return x == reversed_half or x == reversed_half // 10

# Example usage:
if __name__ == '__main__':
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (12321, True),
        (123321, True),
        (12345, False)
    ]
    
    for x, expected in test_cases:
        result1 = is_palindrome_str(x)
        result2 = is_palindrome(x)
        print(f'Input: x = {x}')
        print(f'Expected: {expected}')
        print(f'String method: {result1} {
PASS if result1 == expected else FAIL}')
        print(f'Math method:   {result2} {PASS if result2 == expected else FAIL}')
        print()

