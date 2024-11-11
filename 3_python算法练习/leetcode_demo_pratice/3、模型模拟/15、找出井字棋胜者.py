class Solution(object):
    def tictactoe(self,moves):
        grid = [[' ' for _ in range(3)] for _ in range(3)]

        # 玩家标志
        player = 'X'

        for move in moves:
            row, col = move
            grid[row][col] = player

            # 检查行、列和对角线是否获胜
            if (
                    all(grid[row][c] == player for c in range(3)) or
                    all(grid[r][col] == player for r in range(3)) or
                    (row == col and all(grid[i][i] == player for i in range(3))) or
                    (row + col == 2 and all(grid[s][2 - s] == player for s in range(3)))
            ):
                return 'A' if player == 'X' else 'B'

            # 交换玩家
            player = 'O' if player == 'X' else 'X'

        # 如果所有格子都填满
        if len(moves) == 9:
            return "Draw"

        return "Pending"


# 示例用法
moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
s = Solution()
print(s.tictactoe(moves))  # 输出 "A"