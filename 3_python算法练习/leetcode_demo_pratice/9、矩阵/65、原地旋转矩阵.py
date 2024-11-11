def rotate(matrix):
    n = len(matrix)

    # 1. 转置矩阵
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 2. 翻转每一行
    for i in range(n):
        matrix[i].reverse()


# 输入矩阵
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 旋转矩阵
rotate(matrix)

# 输出结果
print(matrix)