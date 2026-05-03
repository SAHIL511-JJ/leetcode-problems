"""
LeetCode #20: Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
"""


def is_valid_parentheses(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else "#"
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return not stack


if __name__ == "__main__":
    tests = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for t in tests:
        print(f"'{t}': {is_valid_parentheses(t)}")
