class Solution(object):
    def countOdds(self, low, high):
        # 输出low和high之间奇数的数目
        count = (high - low) // 2
        if low % 2 != 0 or high % 2 != 0:
            count = count + 1
        return count

    def countOdds2(self, low, high):
        # 输出low和high之间所有的奇数
        # 初始化一个列表，用于存储奇数
        odds = []
        # 遍历从 low 到 high 的所有整数
        for num in range(low, high + 1):
            # 检查当前数是否是奇数
            if num % 2 != 0:
                odds.append(num)
        return odds

low = 8
high = 10
print(Solution().countOdds(low, high))


