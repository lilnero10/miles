class Solution(object):
    def largestPerimeter(self, nums):
        # 先对数组进行排序
        nums.sort()

        # 从最大的三个数开始，逐步向前检查是否能组成三角形
        for i in range(len(nums) - 1, 1, -1):
            # range（start, stop, 步长）

            if nums[i] < nums[i - 1] + nums[i - 2]:
                return nums[i] + nums[i - 1] + nums[i - 2]
                # 求周长

        # 如果找不到满足条件的三角形，返回0
        return 0


# 示例
nums = [1, 2, 1, 10, 9, 17]
print(Solution().largestPerimeter(nums))
# Solution().largestPerimeter(nums)