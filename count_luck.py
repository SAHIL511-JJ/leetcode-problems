#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#

def countLuck(matrix, k):
    """
    Determine if Hermione used her wand exactly k times to reach the exit.
    She uses her wand when there are multiple paths to choose from.
    """
    n = len(matrix)
    m = len(matrix[0])
    
    # Find start and end positions
    start = end = None
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'M':
                start = (i, j)
            elif matrix[i][j] == '*':
                end = (i, j)
    
    def count_neighbors(i, j, visited):
        """Count valid unvisited neighbors"""
        count = 0
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if (0 <= ni < n and 0 <= nj < m and 
                (ni, nj) not in visited and matrix[ni][nj] != 'X'):
                count += 1
        return count
    
    def dfs(i, j, visited, wand_count):
        """DFS to find path and count wand uses"""
        if (i, j) == end:
            return wand_count
        
        visited.add((i, j))
        
        # Count valid neighbors (decision points)
        neighbors = count_neighbors(i, j, visited)
        
        # If more than one choice, Hermione uses her wand
        if neighbors > 1:
            wand_count += 1
        
        # Try all directions
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if (0 <= ni < n and 0 <= nj < m and 
                (ni, nj) not in visited and matrix[ni][nj] != 'X'):
                result = dfs(ni, nj, visited, wand_count)
                if result is not None:
                    return result
        
        visited.remove((i, j))
        return None
    
    wand_uses = dfs(start[0], start[1], set(), 0)
    
    return "Impressed" if wand_uses == k else "Oops!"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    t = int(input().strip())
    
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        
        matrix = []
        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)
        
        k = int(input().strip())
        
        result = countLuck(matrix, k)
        
        fptr.write(result + '\n')
    
    fptr.close()
