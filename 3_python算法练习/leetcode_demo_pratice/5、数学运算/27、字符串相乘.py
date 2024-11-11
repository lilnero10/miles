class Solution(object):
    def multiply(self,num1, num2):
        # 判断字符串是否为0
        if num1 == "0" or num2 == "0":
            return "0"

        # 初始化数组：result 数组的长度为 m + n，其中 m 和 n 分别为 num1 和 num2 的长度
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        # return result

        # 双重循环从字符串的末尾开始逐位相乘，将乘积结果累加到 result 数组的对应位置上
        for i in range(m - 1, -1, -1):
            # print(i)
            for j in range(n - 1, -1, -1):
                # print(j)
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                # print(num1[i])
                # print(num2[j])
                # print(mul)
                # print(result[i + j + 1])
                total = mul + result[i + j + 1]
                # print(total)
                result[i + j] += total // 10
                # print(result[i + j])
                result[i + j + 1] = total % 10
                # print(result[i + j + 1])

        # 处理进位：每次乘积后需要将结果进行进位处理，确保每个位置上的数字不超过单个数字的位数
        if result[0] == 0:
            result = result[1:]
            print(result[1:])

        # 移除前导零：最后将 result 数组转换为字符串，如果最高位是0则移除前导零
        return ''.join(map(str, result))

    def multiply2(self, num1, num2):
        return str(int(num1) * int(num2))

# 示例
num1 = "123"
num2 = "4"
print(Solution().multiply(num1, num2))
