#!/usr/bin/env python3
"""
HackerRank: Bubble Sort
https://www.hackerrank.com/challenges/ctci-bubble-sort

Given an array, sort it using bubble sort and count total swaps.
Print results including first and last elements.
"""

def count_swaps(a):
    """
    Sort array using bubble sort and count swaps.
    
    Args:
        a: list of integers
    """
    n = len(a)
    swaps = 0
    
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    count_swaps(a)
