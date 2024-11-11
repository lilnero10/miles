class Solution(object):
    def maxmunWealth(self, accounts):
        max_wealth = 0

        for account in accounts:
            current_wealth = sum(account)

            if current_wealth > max_wealth:
                max_wealth = current_wealth

        return max_wealth



# 示例用法
accounts1 = [[1, 2, 3], [3, 2, 1]]
accounts2 = [[1, 5], [7, 3], [3, 5]]
s = Solution()
print(s.maxmunWealth(accounts1))  # 输出: 6
print(s.maxmunWealth(accounts2))  # 输出: 10



