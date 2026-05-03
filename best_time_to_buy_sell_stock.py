"""
LeetCode #121: Best Time to Buy and Sell Stock
Find the maximum profit from a single buy and sell transaction.
You must buy before you sell.
"""


def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


def max_profit_with_days(prices):
    """Returns max profit along with buy and sell day indices."""
    min_price = float("inf")
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i, price in enumerate(prices):
        if price < min_price:
            min_price = price
            buy_day = i
        elif price - min_price > max_profit:
            max_profit = price - min_price
            sell_day = i

    return max_profit, buy_day, sell_day


if __name__ == "__main__":
    test = [7, 1, 5, 3, 6, 4]
    result = max_profit(test)
    print(f"Maximum Profit: {result}")
