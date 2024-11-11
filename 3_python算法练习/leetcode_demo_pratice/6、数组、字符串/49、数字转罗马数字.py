class Solution(object):
    def int_to_roman(self,num):
        # 定义罗马数字符号及其对应的值
        val = [
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
        ]

        roman_numeral = ""
        i = 0

        while num > 0:
            # 从最大的值开始逐个匹配
            for _ in range(num // val[i]):
                roman_numeral += syms[i]
                num -= val[i]
            i += 1

        return roman_numeral

    # 测试示例
    num = 3749
    print(int_to_roman(num))  # 输出: "MMMDCCXLIX"