#!/usr/bin/env python3
"""
HackerRank: Compare the Triplets
https://www.hackerrank.com/challenges/compare-the-triplets

Alice and Bob each created one problem for a contest.
Compare their ratings and return the comparison points.
"""

def compare_triplets(a, b):
    """
    Compare ratings and return points.
    
    Args:
        a: Alice's ratings [a1, a2, a3]
        b: Bob's ratings [b1, b2, b3]
    
    Returns:
        List [alice_points, bob_points]
    """
    alice = 0
    bob = 0
    
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif b[i] > a[i]:
            bob += 1
    
    return [alice, bob]


if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = compare_triplets(a, b)
    print(' '.join(map(str, result)))
