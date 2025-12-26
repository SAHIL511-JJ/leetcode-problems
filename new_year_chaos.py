#!/usr/bin/env python3
"""
HackerRank: New Year Chaos
https://www.hackerrank.com/challenges/new-year-chaos

People are queued for a ride. Each person can bribe the person in front 
at most 2 times. Given the final queue, determine minimum bribes or 
print "Too chaotic" if someone bribed more than 2 people.
"""

def minimum_bribes(q):
    """
    Calculate minimum bribes or detect chaos.
    
    Args:
        q: final queue positions (1-indexed values)
    
    Prints:
        Minimum bribes or "Too chaotic"
    """
    bribes = 0
    
    for i in range(len(q)):
        # Check if person moved more than 2 positions forward
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        
        # Count how many people with larger numbers are in front
        # Only need to check from max(0, q[i]-2) to i
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    
    print(bribes)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        q = list(map(int, input().split()))
        minimum_bribes(q)
