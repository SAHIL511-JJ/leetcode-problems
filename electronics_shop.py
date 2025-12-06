#!/usr/bin/env python3
"""
HackerRank: Electronics Shop
https://www.hackerrank.com/challenges/electronics-shop

A person wants to spend as much money as possible on one keyboard and one USB drive
with a budget of b dollars. Given price lists for keyboards and USB drives,
find the maximum amount that can be spent, or -1 if nothing can be bought.
"""

def get_money_spent(keyboards, drives, b):
    """
    Find maximum money that can be spent on one keyboard and one USB drive.
    
    Args:
        keyboards: list of keyboard prices
        drives: list of USB drive prices
        b: budget
    
    Returns:
        Maximum money spent, or -1 if no valid purchase exists
    """
    max_spent = -1
    
    for keyboard_price in keyboards:
        for drive_price in drives:
            total = keyboard_price + drive_price
            if total <= b and total > max_spent:
                max_spent = total
    
    return max_spent


if __name__ == '__main__':
    b, n, m = map(int, input().split())
    keyboards = list(map(int, input().split()))
    drives = list(map(int, input().split()))
    
    money_spent = get_money_spent(keyboards, drives, b)
    print(money_spent)
