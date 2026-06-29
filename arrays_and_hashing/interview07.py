"""
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_profit
    

# improved version

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = prices[0]
        for price in prices:
            if price < l:
                l = price
            else:
                max_profit = max(max_profit, price - l)
        return max_profit 
