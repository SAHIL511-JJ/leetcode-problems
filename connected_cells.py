#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    """
    Find the size of the largest connected region of 1s in a binary matrix.
    """
    n = len(matrix)
    m = len(matrix[0])
    visited = [[False] * m for _ in range(n)]
    
    def dfs(i, j):
        """DFS to count connected cells"""
        if (i < 0 or i >= n or j < 0 or j >= m or 
            visited[i][j] or matrix[i][j] == 0):
            return 0
        
        visited[i][j] = True
        count = 1
        
        # Check all 8 directions
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                count += dfs(i + di, j + dj)
        
        return count
    
    max_region = 0
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                region_size = dfs(i, j)
                max_region = max(max_region, region_size)
    
    return max_region

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input().strip())
    m = int(input().strip())
    
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))
    
    result = connectedCell(matrix)
    
    fptr.write(str(result) + '\n')
    fptr.close()
