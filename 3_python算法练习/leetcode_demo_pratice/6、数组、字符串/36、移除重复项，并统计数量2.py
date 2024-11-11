"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过"两次"的元素只出现"两次" ，返回删除后数组的新长度
"""
class Solution(object):
    def removeDuplicates(self,nums):
        if len(nums) <= 2:
            return len(nums)

        # 初始化慢指针
        slow = 2

        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow

# 示例用法
# nums1 = [1, 1, 1, 2, 2, 3]
nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]

# 调用函数并输出结果
# k1 = Solution().removeDuplicates(nums1)
k2 = Solution().removeDuplicates(nums2)

# print(k1)  # 输出: 5
# print(nums1[:k1])  # 输出: [1, 1, 2, 2, 3]

# print(k2)  # 输出: 7
# print(nums2[:k2])  # 输出: [0, 0, 1, 1, 2, 3, 3]