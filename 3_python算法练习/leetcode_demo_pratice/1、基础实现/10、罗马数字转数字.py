class Solution(object):
    def roman_to_int(self,s):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        for char in s:
            value = roman_dict[char]
            if value > prev_value:
                result += value - 2 * prev_value
            else:
                result += value
            prev_value = value
        return result

# 测试示例
s1 = "III"
s2 = "IV"
s3 = "IX"
s4 = "LVIII"
s5 = "MCMXCIV"
s = Solution()
print(s.roman_to_int(s1))  # 输出 3
print(s.roman_to_int(s2))  # 输出 4
print(s.roman_to_int(s3))  # 输出 9
print(s.roman_to_int(s4))  # 输出 58
print(s.roman_to_int(s5))  # 输出 1994