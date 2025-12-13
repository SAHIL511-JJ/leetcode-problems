#!/usr/bin/env python3
"""
HackerRank: Birthday Cake Candles
https://www.hackerrank.com/challenges/birthday-cake-candles

You can only blow out the tallest candles.
Count the number of tallest candles.
"""

def birthday_cake_candles(candles):
    """
    Count tallest candles.
    
    Args:
        candles: list of candle heights
    
    Returns:
        Count of tallest candles
    """
    max_height = max(candles)
    return candles.count(max_height)


if __name__ == '__main__':
    n = int(input())
    candles = list(map(int, input().split()))
    result = birthday_cake_candles(candles)
    print(result)
