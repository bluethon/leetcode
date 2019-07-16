#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心
        # 边界处理
        if not prices or len(prices) == 1:
            return 0
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit
