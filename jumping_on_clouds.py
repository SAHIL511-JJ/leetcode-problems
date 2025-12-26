#!/usr/bin/env python3
"""
HackerRank: Jumping on the Clouds
https://www.hackerrank.com/challenges/jumping-on-the-clouds

Emma is playing a game where she must jump on clouds avoiding thunderheads.
Find the minimum number of jumps to reach the last cloud.
Clouds can be safe (0) or thunderheads (1). Can jump 1 or 2 clouds.
"""

def jumping_on_clouds(c):
    """
    Find minimum jumps to reach last cloud.
    
    Args:
        c: list of cloud types (0=safe, 1=thunderhead)
    
    Returns:
        Minimum number of jumps
    """
    n = len(c)
    jumps = 0
    i = 0
    
    while i < n - 1:
        # Try to jump 2 clouds if possible
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    
    return jumps


if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().split()))
    result = jumping_on_clouds(c)
    print(result)
