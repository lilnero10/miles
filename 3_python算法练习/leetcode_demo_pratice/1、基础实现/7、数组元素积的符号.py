class Solution(object):
    def arraySign(self,nums):
        product = 1
        for num in nums:
            product *= num
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0

nums = [-1,1,-1,1,-1]
s = Solution()
print(s.arraySign(nums))