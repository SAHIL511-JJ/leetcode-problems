#!/bin/python3

import math
import os

def encryption(s):
    """
    Encrypt a string by arranging it in a grid and reading column by column.
    Grid dimensions: rows × columns where floor(√L) ≤ rows ≤ columns ≤ ceil(√L)
    
    Args:
        s: String to encrypt (spaces removed)
    
    Returns:
        Encrypted string with spaces between column readings
    """
    # Remove spaces
    s = s.replace(' ', '')
    L = len(s)
    
    # Calculate grid dimensions
    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))
    
    # Ensure rows * cols >= L
    if rows * cols < L:
        rows = cols
    
    # Build encrypted string by reading columns
    encrypted = []
    for col in range(cols):
        column_chars = ''
        for row in range(rows):
            index = row * cols + col
            if index < L:
                column_chars += s[index]
        encrypted.append(column_chars)
    
    return ' '.join(encrypted)

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')
    s = input()
    result = encryption(s)
    fptr.write(result + '\n')
    fptr.close()
