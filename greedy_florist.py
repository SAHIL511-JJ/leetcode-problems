#!/usr/bin/env python3
"""
HackerRank: Greedy Florist
https://www.hackerrank.com/challenges/greedy-florist

A florist increases prices for repeat customers.
Find minimum cost to buy all flowers with k friends.
"""

def get_minimum_cost(k, c):
    """
    Find minimum cost to buy all flowers.
    
    Args:
        k: number of friends
        c: list of flower costs
    
    Returns:
        Minimum total cost
    """
    # Sort flowers by cost descending (buy expensive ones first)
    c.sort(reverse=True)
    
    total_cost = 0
    for i, cost in enumerate(c):
        # Multiplier increases after each round of k purchases
        multiplier = (i // k) + 1
        total_cost += multiplier * cost
    
    return total_cost


if __name__ == '__main__':
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    result = get_minimum_cost(k, c)
    print(result)
