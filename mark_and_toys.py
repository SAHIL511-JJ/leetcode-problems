#!/usr/bin/env python3
"""
HackerRank: Mark and Toys
https://www.hackerrank.com/challenges/mark-and-toys

Mark has a budget and wants to buy as many toys as possible.
Given a list of toy prices and a budget, find maximum toys.
"""

def maximum_toys(prices, k):
    """
    Find maximum number of toys within budget.
    
    Args:
        prices: list of toy prices
        k: budget
    
    Returns:
        Maximum number of toys
    """
    prices.sort()
    count = 0
    total = 0
    
    for price in prices:
        if total + price <= k:
            total += price
            count += 1
        else:
            break
    
    return count


if __name__ == '__main__':
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    result = maximum_toys(prices, k)
    print(result)
