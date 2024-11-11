class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # 如果 k 大于 n，则取 k 对 n 的模
        nums[:] = nums[-k:] + nums[:-k]

    def rotate2(self, nums, k):
        length = len(nums)
        k = k % length
        # nums.extend(nums)
        # nums = nums[length-k:length+k]
        tmp = nums[:length - k]
        nums[:k] = nums[length - k:]
        nums[k:] = tmp


# 示例用法
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
print(nums)