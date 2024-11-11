class Solution(object):
    #  def judgeline(self,coordinates):
    # 自己写的方法，依托答辩
    #     for i in coordinates:
    #         if (((coordinates[i+1][i] - coordinates[i][i])/(coordinates[i+1][i+1] - coordinates[i][i+1]) !=
    #                 (coordinates[1][0] - coordinates[0][0])/(coordinates[1][1] - coordinates[0][1]))
    #                 or len(coordinates[i]) < 2
    #                 or set(coordinates[i]) == 1):
    #             return False
    #         elif ((coordinates[i+1][i] - coordinates[i][i])/(coordinates[i+1][i+1] - coordinates[i][i+1]) ==
    #                 (coordinates[1][0] - coordinates[0][0])/(coordinates[1][1] - coordinates[0][1])):
    #             if coordinates[1][1] - coordinates[0][1] == 0:
    #                 return False
    #             else:
    #                 xl = (coordinates[1][0] - coordinates[0][0]) / (coordinates[1][1] - coordinates[0][1])
    #                 return xl
    def judgeline(self,coordinates):
        if len(coordinates) < 2:
            return True

        # 取前两个点作为起始点
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        # 计算起始斜率
        if x2 - x1 == 0:
            slope = float('inf')  # 处理斜率为无穷大的情况（垂直线）
        else:
            slope = (y2 - y1) / (x2 - x1)

        # 检查剩余点是否共线
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if x2 - x1 == 0:
                if x - x1 != 0:
                    return False
            else:
                if (y - y1) / (x - x1) != slope:
                    return False

        return True

coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(Solution().judgeline(coordinates))