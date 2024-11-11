class Solution(object):
    def sumbinary3(self, a, b):
        # 秒了
        return str(bin(int(a, 2) + int(b, 2)))[2:]

    def sumbinary(self,a,b):
        a1 = int(a,2)
        b1 = int(b,2)
        c = a1 + b1
        binary_str = bin(c)[2:]
        return binary_str

    def sumbinary2(self,a, b):
        result = []  # 用于存储结果的列表
        carry = 0  # 进位初始化为0

        # 从末尾开始逐位相加
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            # 取当前位的值，如果超出索引则取0
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            # 计算当前位的和
            sum_bits = bit_a + bit_b + carry

            # 计算当前位的结果和进位
            result.append(str(sum_bits % 2))  # 当前位的结果
            carry = sum_bits // 2  # 计算进位

            # 移动到下一位
            i -= 1
            j -= 1

        # 将列表中的结果逆序并连接为字符串
        return ''.join(result[::-1])


a = '11011'
b = '1010001'
print(Solution().sumbinary(a,b))