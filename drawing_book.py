#!/usr/bin/env python3
"""
HackerRank: Drawing Book
https://www.hackerrank.com/challenges/drawing-book

A teacher gives a student a book with n pages. The student wants to turn to page p.
They can start from the front (page 1) or the back (page n).
Each page turn shows two pages (except the first and last covers).

Find the minimum number of page turns to reach page p.
"""

def page_count(n, p):
    """
    Find minimum page turns to reach page p.
    
    Args:
        n: total number of pages
        p: target page
    
    Returns:
        Minimum number of page turns
    """
    # Turns from the front (page 1 is on the right of first opening)
    from_front = p // 2
    
    # Turns from the back
    # If n is even, last page is alone on the left
    # If n is odd, last page is on the right with n-1 on the left
    from_back = (n // 2) - (p // 2)
    
    return min(from_front, from_back)


if __name__ == '__main__':
    n = int(input())
    p = int(input())
    result = page_count(n, p)
    print(result)
