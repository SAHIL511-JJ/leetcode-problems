#!/usr/bin/env python3
"""
HackerRank: Frequency Queries
https://www.hackerrank.com/challenges/frequency-queries

Perform operations on a data structure:
1 x: Insert x
2 x: Delete one occurrence of x
3 x: Check if any element has frequency x
"""

from collections import defaultdict

def freq_query(queries):
    """
    Process frequency queries.
    
    Args:
        queries: list of [operation, value] pairs
    
    Returns:
        List of results for operation 3
    """
    data = defaultdict(int)      # element -> frequency
    freq_count = defaultdict(int) # frequency -> count of elements
    results = []
    
    for op, val in queries:
        if op == 1:
            # Decrease old frequency count
            if data[val] > 0:
                freq_count[data[val]] -= 1
            # Insert
            data[val] += 1
            freq_count[data[val]] += 1
            
        elif op == 2:
            # Delete one occurrence
            if data[val] > 0:
                freq_count[data[val]] -= 1
                data[val] -= 1
                if data[val] > 0:
                    freq_count[data[val]] += 1
                    
        else:  # op == 3
            # Check if any element has frequency val
            if freq_count[val] > 0:
                results.append(1)
            else:
                results.append(0)
    
    return results


if __name__ == '__main__':
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    result = freq_query(queries)
    print('\n'.join(map(str, result)))
