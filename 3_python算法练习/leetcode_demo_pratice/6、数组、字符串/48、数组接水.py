class Solution(object):
    def trap(self,height):
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
                print(water_trapped, left_max, height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
                print(water_trapped, right_max, height[right])


        return water_trapped

# 示例 1
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height1))  # 输出：6

# # 示例 2
# height2 = [4, 2, 0, 3, 2, 5]
# print(Solution().trap(height2))  # 输出：9