class Solution(object):
    def spiralOrder(self,matrix):
    # 顺时针输出
        # if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        #     print("错误，输入的不是矩阵")
        #     return []
        if not matrix:
            return []

        result = []
        # m:行数 n：列数
        m, n = len(matrix), len(matrix[0])
        # left, right, top, bottom 分别表示当前边界的左右上下
        left, right, top, bottom = 0, n - 1, 0, m - 1

        while left <= right and top <= bottom:
            # 从矩阵的左上角开始，首先遍历矩阵的上边界
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # 遍历矩阵的右边界
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # 遍历矩阵的下边界
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # 遍历矩阵的左边界
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

    def counterclockwise(matrix):
    # 逆时针输出
        if not matrix:
            return []

        result = []
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1

        while top <= bottom and left <= right:
            # 从右上到右下
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # 从右下到左下
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # 从左下到左上
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

            # 从左上到右上
            if top <= bottom:
                for i in range(left, right + 1):
                    result.append(matrix[top][i])
                top += 1

        return result




    # 示例用法
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
matrix3 = [
    [1,2,3],
    [4,5],
    [6,7,8]
]
s = Solution()
print(s.spiralOrder(matrix1))
print(s.spiralOrder(matrix2))
print(s.spiralOrder(matrix3))

