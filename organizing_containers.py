#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    """
    Determine if it's possible to organize containers so each contains only one type of ball.
    """
    n = len(container)
    
    # Calculate capacity of each container (total balls it can hold)
    container_capacities = [sum(container[i]) for i in range(n)]
    
    # Calculate total balls of each type
    ball_type_counts = [sum(container[i][j] for i in range(n)) for j in range(n)]
    
    # Sort both lists and compare
    # If they match, we can organize; otherwise impossible
    container_capacities.sort()
    ball_type_counts.sort()
    
    return "Possible" if container_capacities == ball_type_counts else "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    q = int(input().strip())
    
    for q_itr in range(q):
        n = int(input().strip())
        
        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))
        
        result = organizingContainers(container)
        
        fptr.write(result + '\n')
    
    fptr.close()
