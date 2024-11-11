def plusOne(digits):
    # 从数组末尾开始遍历
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    # 如果循环结束仍未返回，说明需要在最高位添加一个进位
    return [1] + digits

digits = [1, 2, 3]
print(plusOne(digits))