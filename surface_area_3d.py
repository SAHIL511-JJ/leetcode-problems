#!/bin/python3

import os

def surfaceArea(A):
    """
    Calculate the surface area of a 3D structure made of 1x1x1 cubes.
    
    Args:
        A: 2D array where A[i][j] represents height of cube stack
    
    Returns:
        Total surface area
    """
    H = len(A)
    W = len(A[0])
    total_area = 0
    
    for i in range(H):
        for j in range(W):
            if A[i][j] > 0:
                # Top and bottom faces
                total_area += 2
                
                # Front face
                if i == 0:
                    total_area += A[i][j]
                else:
                    total_area += max(0, A[i][j] - A[i-1][j])
                
                # Back face
                if i == H - 1:
                    total_area += A[i][j]
                else:
                    total_area += max(0, A[i][j] - A[i+1][j])
                
                # Left face
                if j == 0:
                    total_area += A[i][j]
                else:
                    total_area += max(0, A[i][j] - A[i][j-1])
                
                # Right face
                if j == W - 1:
                    total_area += A[i][j]
                else:
                    total_area += max(0, A[i][j] - A[i][j+1])
    
    return total_area

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')
    first_multiple_input = input().rstrip().split()
    H = int(first_multiple_input[0])
    W = int(first_multiple_input[1])
    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))
    result = surfaceArea(A)
    fptr.write(str(result) + '\n')
    fptr.close()
