class Solution():
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            # 计算当前容积
            current_water = (right - left) * min(height[left], height[right])
            max_water = max(max_water, current_water)

            # 移动较小的高度指针
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

# 示例使用
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(heights))