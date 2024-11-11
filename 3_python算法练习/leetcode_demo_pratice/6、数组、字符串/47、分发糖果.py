"""
n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
你需要按照以下要求，给这些孩子分发糖果：
每个孩子至少分配到 1 个糖果。
相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目
"""
class Solution(object):
    def candy(self,ratings):
        n = len(ratings)
        if n == 0:
            return 0

        candies = [1] * n

        # 从左到右扫描
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # 从右到左扫描
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)

# 示例 1
ratings1 = [1, 0, 2]
print(Solution().candy(ratings1))  # 输出: 5

# 示例 2
ratings2 = [1, 2, 2]
print(Solution().candy(ratings2))  # 输出: 4