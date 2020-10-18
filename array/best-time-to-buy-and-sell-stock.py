"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


def best_trade_brute_force(prices):
    maxprofit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > maxprofit:
                maxprofit = profit
    return maxprofit


def best_trade_one_pass(prices):
    import sys
    minprice = sys.maxsize
    maxprofit = 0
    for i in range(len(prices)):
        if prices[i] < minprice:
            minprice = prices[i]
        elif prices[i] - minprice > maxprofit:
            maxprofit = prices[i] - minprice
    return maxprofit


prices = [7, 1, 5, 3, 6, 4]
print("Best trade brute force")
print(best_trade_brute_force(prices))
print("Best trade one-pass")
print(best_trade_one_pass(prices))

prices = [7, 6, 4, 3, 1]
print("Best trade brute force")
print(best_trade_brute_force(prices))
print("Best trade one-pass")
print(best_trade_one_pass(prices))
