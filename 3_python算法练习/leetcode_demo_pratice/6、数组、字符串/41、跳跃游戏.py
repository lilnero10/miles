"""
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false
"""
class Solution(object):
    def canJump(self,nums):
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
        return True

# 示例用法
nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
print(Solution().canJump(nums1))
print(Solution().canJump(nums2))