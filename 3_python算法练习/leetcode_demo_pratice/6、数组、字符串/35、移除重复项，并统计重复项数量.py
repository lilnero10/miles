"""
给你一个非严格递增排列的数组nums ，请你原地删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。
元素的相对顺序应该保持一致 。然后返回 nums 中唯一元素的个数
"""
class Solution(object):
    # def pop_num(self, nums, val):
    # 自己写的代码，依托答辩
    #     i = 0
    #     x = 0
    #     while i < len(nums):
    #         if nums[i] == val:
    #             nums.pop(i)
    #             # 当 pop 函数带一个参数时，它移除并返回该位置的元素
    #             x += 1
    #         else:
    #             i += 1
    #     return i,x

    def removeDuplicates(self,nums):
        if not nums:
            return 0

        # 初始化慢指针
        slow = 0

        # 遍历数组
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        # 新数组长度为 slow 指针位置 + 1
        return slow + 1

# 示例用法
nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# 调用函数并输出结果
k1 = Solution().removeDuplicates(nums1)
k2 = Solution().removeDuplicates(nums2)

print(k1)  # 输出: 2
print(nums1[:k1])  # 输出: [1, 2]

print(k2)  # 输出: 5
print(nums2[:k2])  # 输出: [0, 1, 2, 3, 4]

