#!/usr/bin/env python3
"""
HackerRank: Counting Valleys
https://www.hackerrank.com/challenges/counting-valleys

A hiker tracks their path with U (uphill) and D (downhill) steps.
A valley is a sequence of consecutive steps below sea level, starting with D
and ending with U back to sea level.

Count the number of valleys traversed.
"""

def counting_valleys(steps, path):
    """
    Count the number of valleys traversed.
    
    Args:
        steps: number of steps in the hike
        path: string of 'U' and 'D' representing the path
    
    Returns:
        Number of valleys traversed
    """
    level = 0
    valleys = 0
    
    for step in path:
        if step == 'U':
            level += 1
            # Returning to sea level from below means we completed a valley
            if level == 0:
                valleys += 1
        else:  # step == 'D'
            level -= 1
    
    return valleys


if __name__ == '__main__':
    steps = int(input())
    path = input()
    result = counting_valleys(steps, path)
    print(result)
