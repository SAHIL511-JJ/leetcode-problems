#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    """
    Simulate the Bomberman game for n seconds.
    """
    if n == 1:
        return grid
    
    if n % 2 == 0:
        # All cells filled with bombs
        return ['O' * len(grid[0]) for _ in range(len(grid))]
    
    r, c = len(grid), len(grid[0])
    
    def detonate(g):
        """Detonate bombs and return new grid"""
        new_grid = [['O'] * c for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                if g[i][j] == 'O':
                    # Bomb explodes, destroy itself and adjacent cells
                    new_grid[i][j] = '.'
                    if i > 0:
                        new_grid[i-1][j] = '.'
                    if i < r - 1:
                        new_grid[i+1][j] = '.'
                    if j > 0:
                        new_grid[i][j-1] = '.'
                    if j < c - 1:
                        new_grid[i][j+1] = '.'
        
        return [''.join(row) for row in new_grid]
    
    # Pattern repeats every 4 seconds after second 1
    # n=3: first detonation
    # n=5: second detonation (same as n=3)
    # n=7: third detonation (same as n=3)
    
    grid1 = detonate(grid)  # State at n=3
    grid2 = detonate(grid1)  # State at n=5
    
    if n % 4 == 3:
        return grid1
    else:  # n % 4 == 1 and n > 1
        return grid2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    first_multiple_input = input().rstrip().split()
    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    n = int(first_multiple_input[2])
    
    grid = []
    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)
    
    result = bomberMan(n, grid)
    
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
