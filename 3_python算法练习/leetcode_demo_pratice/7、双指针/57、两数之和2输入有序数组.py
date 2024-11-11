class Solution():
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # 返回1-based index
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []  # 不应该到达这里，如果有唯一的解决方案

numbers = [2,7,11,15]
target = 9
print(Solution().twoSum(numbers, target))