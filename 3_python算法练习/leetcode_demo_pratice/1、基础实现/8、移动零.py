class Solution(object):
    def moveZeroes(self, nums) -> object:
        non_zero_index = 0  # 记录非零元素的位置
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                if i != non_zero_index:
                    nums[i] = 0
                non_zero_index += 1
        return nums

s = Solution()
nums = [0, 1, 0, 3, 12] # 输出 [1, 3, 12, 0, 0]
print(s.moveZeroes(nums))

# def moveZeroes(self, nums: List[int]) -> None:
#
#     for i in range(len(nums)):
#
#         if nums[i]==0:
#
#             nums.remove(0)
#
#             nums.append(0)