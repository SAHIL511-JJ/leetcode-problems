#!/usr/bin/env python3
"""
HackerRank: Array Manipulation
https://www.hackerrank.com/challenges/crush

Starting with a 1-indexed array of zeros and a list of operations,
for each operation add a value to each element between two given indices.
Return the maximum value in the array after all operations.
"""

def array_manipulation(n, queries):
    """
    Find maximum value after range updates using difference array.
    
    Args:
        n: size of array
        queries: list of [a, b, k] operations
    
    Returns:
        Maximum value in final array
    """
    # Use difference array technique for O(n + m) solution
    arr = [0] * (n + 2)
    
    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k
    
    # Find max by computing prefix sum
    max_val = 0
    running_sum = 0
    for val in arr:
        running_sum += val
        max_val = max(max_val, running_sum)
    
    return max_val


if __name__ == '__main__':
    n, m = map(int, input().split())
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().split())))
    result = array_manipulation(n, queries)
    print(result)
