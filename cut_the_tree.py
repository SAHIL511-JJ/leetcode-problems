#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

def cutTheTree(data, edges):
    """
    Find the minimum difference when cutting one edge from the tree.
    """
    n = len(data)
    
    # Build adjacency list
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Calculate total sum
    total_sum = sum(data)
    
    # Subtree sums
    subtree_sum = [0] * (n + 1)
    
    def dfs(node, parent):
        """Calculate subtree sum for each node"""
        subtree_sum[node] = data[node - 1]  # data is 0-indexed
        
        for neighbor in graph[node]:
            if neighbor != parent:
                subtree_sum[node] += dfs(neighbor, node)
        
        return subtree_sum[node]
    
    # Start DFS from node 1
    dfs(1, -1)
    
    # Find minimum difference
    min_diff = float('inf')
    
    for node in range(1, n + 1):
        # If we cut the edge above this node
        sum1 = subtree_sum[node]
        sum2 = total_sum - sum1
        diff = abs(sum1 - sum2)
        min_diff = min(min_diff, diff)
    
    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input().strip())
    
    data = list(map(int, input().rstrip().split()))
    
    edges = []
    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))
    
    result = cutTheTree(data, edges)
    
    fptr.write(str(result) + '\n')
    fptr.close()
