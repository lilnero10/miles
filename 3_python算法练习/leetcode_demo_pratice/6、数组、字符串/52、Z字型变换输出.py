"""
输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"
"""
def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    # 创建一个列表，每个元素是一个字符串，表示每一行
    rows = [''] * numRows
    current_row = 0
    going_down = False

    # 遍历输入字符串
    for char in s:
        # 将字符添加到当前行
        rows[current_row] += char
        # 如果到达第一行或最后一行，改变方向
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        # 更新当前行索引
        current_row += 1 if going_down else -1

    # 将所有行连接成一个字符串
    return ''.join(rows)


# 示例测试
s1 = "PAYPALISHIRING"
numRows1 = 3
print(convert(s1, numRows1))  # 输出: "PAHNAPLSIIGYIR"

s2 = "PAYPALISHIRING"
numRows2 = 4
print(convert(s2, numRows2))  # 输出: "PINALSIGYAHRPI"