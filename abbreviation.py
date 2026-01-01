#!/usr/bin/env python3
"""
HackerRank: Abbreviation
https://www.hackerrank.com/challenges/abbr

Determine if string a can be transformed to string b by:
1. Capitalizing zero or more lowercase letters
2. Deleting zero or more lowercase letters
"""

def abbreviation(a, b):
    """
    Check if a can be transformed to b.
    
    Args:
        a: source string
        b: target string
    
    Returns:
        'YES' if possible, 'NO' otherwise
    """
    n, m = len(a), len(b)
    
    # dp[i][j] = True if a[:i] can match b[:j]
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(m + 1):
            if a[i-1].isupper():
                # Must match with b[j-1]
                if j > 0 and a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1]
            else:
                # Can capitalize or delete
                # Delete: dp[i-1][j]
                # Capitalize: dp[i-1][j-1] if a[i-1].upper() == b[j-1]
                dp[i][j] = dp[i-1][j]  # Delete
                if j > 0 and a[i-1].upper() == b[j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j-1]
    
    return 'YES' if dp[n][m] else 'NO'


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        a = input()
        b = input()
        result = abbreviation(a, b)
        print(result)
