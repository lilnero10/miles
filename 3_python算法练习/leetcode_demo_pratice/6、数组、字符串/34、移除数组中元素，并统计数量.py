"""
思路：
1、for循环统计重复值，累加数量输出
2、指针
"""
class Solution(object):
    # def removeElement(self, nums, val):
    #     """
    #     :type nums: List[int]
    #     :type val: int
    #     :rtype: int
    #     """
    #     # 初始化结果指针
    #     k = 0
    #     for i in range(1,len(nums)):
    #         if nums[i] != val:
    #             nums[k] = nums[i]
    #             k += 1
    #     return k

    def removeElement(self, nums, val):
        # 初始化两个指针
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                # 如果当前元素等于 val，则将其与数组最后一个有效元素交换
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                # 如果当前元素不等于 val，则移动左指针
                left += 1

        # 返回新数组的长度
        return left


# nums = [1,2,3,4,5,6,7,8,9,2,3,4,1,1]
nums = [0,1,2,2,3,0,4,2]
val = 2
k = Solution().removeElement(nums, val)
print(nums[:k])

def pop_num(nums,val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            # 当 pop 函数带一个参数时，它移除并返回该位置的元素
        else:
            i += 1
    return i