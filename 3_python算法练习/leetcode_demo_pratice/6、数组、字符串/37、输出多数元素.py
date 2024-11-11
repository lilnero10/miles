"""
摩尔投票算法;在一次遍历中有效地统计出数组中出现次数超过一半的元素（多数元素）
"""
class Solution(object):
    def majorityElement(self,nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

# 示例用法
nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]

print(Solution().majorityElement(nums1))
print(Solution().majorityElement(nums2))