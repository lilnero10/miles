from fontTools.qu2cu.qu2cu import Solution


class Solution(object):
    def judgecircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # 计算每个方向的移动次数
        up_count = moves.count('U')
        down_count = moves.count('D')
        left_count = moves.count('L')
        right_count = moves.count('R')

        # 如果向上和向下的次数相同，且向左和向右的次数相同，则返回 True
        return up_count == down_count and left_count == right_count

    # 示例测试
moves = "UD"
s = Solution()
print(s.judgecircle(moves))  # 输出: True