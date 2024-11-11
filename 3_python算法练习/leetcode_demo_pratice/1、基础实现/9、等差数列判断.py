class Solution(object):
    def isMonotonic(self, A):
        return self.isIncreasing(A) or self.isDecreasing(A)

    def isIncreasing(self, A):
        N = len(A)
        for i in range(N - 1):
            if A[i + 1] - A[i] < 0:
                return False
        return True

    def isDecreasing(self, A):
        N = len(A)
        for i in range(N - 1):
            if A[i + 1] - A[i] > 0:
                return False
        return True

# 测试示例
A = [1,2,2,3] #true
s = Solution()
print(s.isMonotonic(A))