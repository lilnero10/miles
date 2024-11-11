"""
双指针从后往前合并数组
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # 设置指针
        p1, p2, p = m - 1, n - 1, m + n - 1

        # 从后往前合并
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # 如果nums2有剩余，直接放入nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        缺点：虽然代码简单，但效率不高。使用 sort 方法进行排序，时间复杂度为 O((m + n) log(m + n))，对于大数组来说不是最优解
        """
        nums1[m:] = nums2
        # nums2 中的所有元素复制到 nums1 从索引 m 开始的位置
        nums1.sort(reverse = False)
        # 对 nums1 进行升序排序
        return nums1
        print("排序成功")

# 示例用法
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)