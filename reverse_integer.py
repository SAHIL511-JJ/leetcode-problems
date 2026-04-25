# Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# Example 1:
#   Input: x = 123
#   Output: 321
#
# Example 2:
#   Input: x = -123
#   Output: -321
#
# Example 3:
#   Input: x = 120
#   Output: 21
#
# Example 4:
#   Input: x = 0
#   Output: 0
#
# Constraints:
#   -2^31 <= x <= 2^31 - 1
#
# Approach:
#   We can convert the integer to a string, reverse it, and convert back to integer.
#   However, we need to handle the sign and check for overflow.
#
#   Steps:
#   1. Store the sign of the number (positive or negative)
#   2. Work with the absolute value of the number
#   3. Convert to string, reverse it, and convert back to integer
#   4. Apply the original sign
#   5. Check if the result is within the 32-bit signed integer range
#   6. If not, return 0; otherwise, return the result
#
#   Time Complexity: O(log(x)) - number of digits in x
#   Space Complexity: O(log(x)) for the string representation

def reverse(x):
    '''
    :type x: int
    :rtype: int
    '''
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648
    
    # Store the sign
    sign = -1 if x < 0 else 1
    
    # Work with absolute value
    x_abs = abs(x)
    
    # Convert to string, reverse, and convert back to int
    reversed_str = str(x_abs)[::-1]
    reversed_int = int(reversed_str)
    
    # Apply the sign
    result = sign * reversed_int
    
    # Check for overflow
    if result < INT_MIN or result > INT_MAX:
        return 0
    
    return result

# Example usage:
if __name__ == '__main__':
    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),  # Overflow case
        (-2147483412, -2147483412)  # Edge case
    ]
    
    for x, expected in test_cases:
        result = reverse(x)
        print(f'Input: x = {x}')
        print(f'Expected: {expected}')
        print(f'Got: {result}')
        print(f'{
PASS if result == expected else FAIL}')
        print()

