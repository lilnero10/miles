class Solution(object):
    def productExceptSelf(self,nums):
        n = len(nums)
        answer = [1] * n
        left = [1] * n
        right = [1] * n

        # 计算前缀积
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # 计算后缀积
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # 计算结果数组
        for i in range(n):
            answer[i] = left[i] * right[i]

        return answer

# 示例用法
nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(nums1))  # 输出: [24, 12, 8, 6]
print(Solution().productExceptSelf(nums2))  # 输出: [0, 0, 9, 0, 0]