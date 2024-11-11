class Solution(object):
    def sumrange(self, mat):
        n = len(mat)
        total_sum = 0

        for i in range(n):
            # 累加主对角线元素
            total_sum += mat[i][i]
            # 累加副对角线元素
            total_sum += mat[i][n-1-i]

        # 如果 n 是奇数，减去重复的中间元素
        if n % 2 == 1:
            total_sum -= mat[n//2][n//2]
        return total_sum

mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
mat2 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
mat3 = [[5]]
s = Solution()
print(s.sumrange(mat1))
print(s.sumrange(mat2))
print(s.sumrange(mat3))

