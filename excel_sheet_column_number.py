# Excel Sheet Column Number
# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#   A -> 1
#   B -> 2
#   C -> 3
#   ...
#   Z -> 26
#   AA -> 27
#   AB -> 28
#   ...
#
# Example 1:
#   Input: columnTitle = \
A\
#   Output: 1
#
# Example 2:
#   Input: columnTitle = \AB\
#   Output: 28
#
# Example 3:
#   Input: columnTitle = \ZY\
#   Output: 701
#
# Constraints:
#   1 <= columnTitle.length <= 7
#   columnTitle consists only of uppercase English letters.
#   columnTitle is in the range [\A\, \FXSHRXW\].
#
# Approach:
#   This is essentially converting a base-26 number to decimal, where A=1, B=2, ..., Z=26.
#   However, unlike standard base conversion where digits go from 0 to 25, here they go from 1 to 26.
#   We can process from left to right:
#     result = result * 26 + (value of current character)
#   where value of char = ord(char) - ord('A') + 1
#
#   Time Complexity: O(n) where n is the length of columnTitle
#   Space Complexity: O(1)

def title_to_number(columnTitle):
    '''
    :type columnTitle: str
    :rtype: int
    '''
    result = 0
    for char in columnTitle:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result

# Example usage:
if __name__ == '__main__':
    test_cases = [
        ('A', 1),
        ('AB', 28),
        ('ZY', 701),
        ('Z', 26),
        ('AA', 27),
        ('FXSHRXW', 2147483647)  # Maximum value according to constraints
    ]
    
    for columnTitle, expected in test_cases:
        result = title_to_number(columnTitle)
        print(f'Input: columnTitle = \
columnTitle
\')
        print(f'Expected: {expected}')
        print(f'Got: {result}')
        print(f'{\PASS\ if result == expected else \FAIL\}')
        print()

