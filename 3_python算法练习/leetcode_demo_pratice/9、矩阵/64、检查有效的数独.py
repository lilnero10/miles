def isValidSudoku(board):
    # 创建集合来存储行、列、子宫格中出现的数字
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue  # 跳过空格

            # 检查行
            if num in rows[i]:
                return False
            rows[i].add(num)

            # 检查列
            if num in columns[j]:
                return False
            columns[j].add(num)

            # 检查 3x3 子宫格
            box_index = (i // 3) * 3 + j // 3
            if num in boxes[box_index]:
                return False
            boxes[box_index].add(num)

    return True


# 输入数独棋盘
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# 验证数独是否有效
print(isValidSudoku(board))  # 输出: True