"""
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
返回 你能获得的 最大 利润
"""
class Solution(object):
    def maxProfit(self,prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

# 示例用法
prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
prices2 = [1,2,3,4,5]
print(Solution().maxProfit(prices2))
prices3 = [7,6,4,3,1]
print(Solution().maxProfit(prices3))
