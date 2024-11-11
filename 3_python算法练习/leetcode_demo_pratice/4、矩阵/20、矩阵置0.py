class Solution(object):
    def setZeroes(self,matrix):
        if not matrix:
            return[]

        m, n = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        # 第一次遍历，记录需要置零的行和列
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # 第二次遍历，置零操作
        for i in range(m):
            for j in range(n):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0

    def setZeroes2(self,matrix):
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # 使用第一行和第一列作为标记
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 根据标记将需要置零的行和列置零
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # 最后处理第一行和第一列
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

# 用函数测试
# def test_setZeroes():
#     matrix = [
#             [1, 1, 1],
#             [1, 0, 1],
#             [1, 1, 1]
#         ]
#     print("输入矩阵:")
#     for row in matrix:
#         print(row)
#
#     sol = Solution()
#     sol.setZeroes2(matrix)
#
#     print("\n输出矩阵:")
#     for row in matrix:
#         print(row)
#
# # 运行测试
# test_setZeroes()

# 用实例测试
matrix = [
    [1, 1, 1, 5, 0],
    [1, 0, 1, 9, 8],
    [1, 1, 1, 9, 9]
]
sol = Solution()
sol.setZeroes(matrix)
print("\n输出矩阵:")
for row in matrix:
    print(row)
# print(matrix)

