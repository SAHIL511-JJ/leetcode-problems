#!/usr/bin/env python3
"""
HackerRank: Plus Minus
https://www.hackerrank.com/challenges/plus-minus

Given an array of integers, calculate the ratios of positive,
negative, and zero elements. Print each ratio on a new line.
"""

def plus_minus(arr):
    """
    Print ratios of positive, negative, and zero elements.
    
    Args:
        arr: list of integers
    """
    n = len(arr)
    positive = sum(1 for x in arr if x > 0)
    negative = sum(1 for x in arr if x < 0)
    zeros = sum(1 for x in arr if x == 0)
    
    print(f'{positive / n:.6f}')
    print(f'{negative / n:.6f}')
    print(f'{zeros / n:.6f}')


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    plus_minus(arr)
