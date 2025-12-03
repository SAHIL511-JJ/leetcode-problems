#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    """
    Calculate the number of squares a queen can attack on an n x n chessboard
    with k obstacles.
    """
    # Convert obstacles to a set for O(1) lookup
    obstacle_set = set((r, c) for r, c in obstacles)
    
    # 8 directions: N, S, E, W, NE, NW, SE, SW
    directions = [
        (-1, 0),  # North
        (1, 0),   # South
        (0, 1),   # East
        (0, -1),  # West
        (-1, 1),  # NE
        (-1, -1), # NW
        (1, 1),   # SE
        (1, -1)   # SW
    ]
    
    total_attacks = 0
    
    # For each direction, count squares until hitting obstacle or board edge
    for dr, dc in directions:
        r, c = r_q, c_q
        while True:
            r += dr
            c += dc
            
            # Check if out of bounds
            if r < 1 or r > n or c < 1 or c > n:
                break
            
            # Check if obstacle
            if (r, c) in obstacle_set:
                break
            
            total_attacks += 1
    
    return total_attacks

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    
    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])
    
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
