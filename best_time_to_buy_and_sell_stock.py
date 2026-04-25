# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Example 1:
#   Input: prices = [7,1,5,3,6,4]
#   Output: 5
#   Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#   Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
#   Input: prices = [7,6,4,3,1]
#   Output: 0
#   Explanation: In this case, no transactions are done and the max profit = 0.
#
# Constraints:
#   1 <= prices.length <= 10^5
#   0 <= prices[i] <= 10^4
#
# Approach:
#   We can iterate through the prices while keeping track of the minimum price seen so far and the maximum profit.
#   For each price, we calculate the profit if we sold at that price (current price - min_so_far) and update max_profit if this profit is larger.
#   Then we update min_so_far if the current price is smaller.
#
#   Time Complexity: O(n) where n is the length of prices
#   Space Complexity: O(1)

def max_profit(prices):
    '''
    :type prices: List[int]
    :rtype: int
    '''
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        # Calculate profit if we sell today
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
        # Update min_price
        if price < min_price:
            min_price = price
    
    return max_profit

# Example usage:
if __name__ == '__main__':
    test_cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1,2,3,4,5], 4),
        ([2,4,1], 2),
        ([1], 0)
    ]
    
    for prices, expected in test_cases:
        result = max_profit(prices)
        print(f'Input: prices = {prices}')
        print(f'Expected: {expected}')
        print(f'Got: {result}')
        print(f'{\
PASS\ if result == expected else \FAIL\}')
        print()

