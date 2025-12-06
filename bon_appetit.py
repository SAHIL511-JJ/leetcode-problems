#!/usr/bin/env python3
"""
HackerRank: Bon Appétit
https://www.hackerrank.com/challenges/bon-appetit

Anna and Brian are sharing a meal at a restaurant. Brian calculates Anna's share
of the bill incorrectly because he includes an item she didn't eat.

Determine if Brian owes Anna money, and if so, how much.
"""

def bon_appetit(bill, k, b):
    """
    Calculate if Brian overcharged Anna.
    
    Args:
        bill: list of item costs
        k: index of item Anna didn't eat
        b: amount Anna contributed
    
    Returns:
        'Bon Appetit' if bill is correct, or the amount Brian owes Anna
    """
    # Anna's fair share (excluding item k)
    total_without_k = sum(bill) - bill[k]
    anna_share = total_without_k // 2
    
    if b == anna_share:
        return 'Bon Appetit'
    else:
        return b - anna_share


if __name__ == '__main__':
    n, k = map(int, input().split())
    bill = list(map(int, input().split()))
    b = int(input())
    
    result = bon_appetit(bill, k, b)
    print(result)
