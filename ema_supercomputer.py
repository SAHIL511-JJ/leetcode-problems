#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    """
    Find two non-overlapping plus signs ('good' pluses) that maximize the product of their areas.
    """
    r, c = len(grid), len(grid[0])
    
    def get_plus_size(i, j):
        """Get maximum size of plus centered at (i, j)"""
        size = 0
        while (i - size >= 0 and i + size < r and 
               j - size >= 0 and j + size < c and
               grid[i - size][j] == 'G' and
               grid[i + size][j] == 'G' and
               grid[i][j - size] == 'G' and
               grid[i][j + size] == 'G'):
            size += 1
        return size - 1
    
    def get_cells(i, j, size):
        """Get all cells occupied by plus centered at (i, j) with given size"""
        cells = {(i, j)}
        for k in range(1, size + 1):
            cells.add((i - k, j))
            cells.add((i + k, j))
            cells.add((i, j - k))
            cells.add((i, j + k))
        return cells
    
    # Find all possible pluses
    pluses = []
    for i in range(r):
        for j in range(c):
            max_size = get_plus_size(i, j)
            for size in range(max_size + 1):
                area = 1 + 4 * size
                cells = get_cells(i, j, size)
                pluses.append((area, cells))
    
    # Find maximum product of two non-overlapping pluses
    max_product = 0
    for i in range(len(pluses)):
        for j in range(i + 1, len(pluses)):
            area1, cells1 = pluses[i]
            area2, cells2 = pluses[j]
            if not cells1 & cells2:  # No overlap
                max_product = max(max_product, area1 * area2)
    
    return max_product

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    
    result = twoPluses(grid)
    
    fptr.write(str(result) + '\n')
    fptr.close()
