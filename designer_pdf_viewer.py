#!/usr/bin/env python3
"""
HackerRank: Designer PDF Viewer
https://www.hackerrank.com/challenges/designer-pdf-viewer

When a contiguous block of text is selected in a PDF viewer, the selection is highlighted
with a blue rectangle. The area of the rectangle is (width * height).

Given a word and height of each letter (a-z), determine the area of the highlighted rectangle.
"""

def designer_pdf_viewer(h, word):
    """
    Calculate the area of the highlighted rectangle.
    
    Args:
        h: list of 26 integers representing heights of letters a-z
        word: the word to highlight
    
    Returns:
        Area of the rectangle (width * max_height)
    """
    max_height = 0
    for char in word:
        index = ord(char) - ord('a')
        max_height = max(max_height, h[index])
    
    width = len(word)
    return width * max_height


if __name__ == '__main__':
    h = list(map(int, input().split()))
    word = input()
    result = designer_pdf_viewer(h, word)
    print(result)
