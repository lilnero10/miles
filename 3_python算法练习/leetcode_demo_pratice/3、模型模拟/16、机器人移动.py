class Solution(object):
    def isRobotBounded(self,instructions: str) -> bool:
        # 方向数组，表示北、东、南、西四个方向
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # 初始化机器人位置和方向索引（0 表示北方）
        x, y = 0, 0
        direction_index = 0

        for instruction in instructions:
            if instruction == 'G':
                x += directions[direction_index][0]
                y += directions[direction_index][1]
                # 机器人根据当前方向移动一格
                # direction_index 表示当前方向在 directions 数组中的索引
                # directions[direction_index] 给出当前方向的变化量
                # 通过 x += directions[direction_index][0] 和 y += directions[direction_index][1] 更新机器人的位置
            elif instruction == 'L':
                direction_index = (direction_index - 1) % 4
                # 机器人左转 90 度
                # direction_index 减 1，表示顺时针方向上前一个方向
                # 使用 (direction_index - 1) % 4 来确保索引在 0 到 3 之间循环
            elif instruction == 'R':
                direction_index = (direction_index + 1) % 4
                # 机器人右转 90 度
                # direction_index 加 1，表示顺时针方向上下一个方向
                # 使用 (direction_index + 1) % 4 来确保索引在 0 到 3 之间循环

        # 如果机器人回到原点或方向不是北方
        return (x == 0 and y == 0) or direction_index != 0

# 示例用法
instructions = "GGLLGG"
s = Solution()
print(s.isRobotBounded(instructions))