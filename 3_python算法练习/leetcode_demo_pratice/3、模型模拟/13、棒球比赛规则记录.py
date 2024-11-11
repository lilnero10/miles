class Solution(object):
    def calPoints(self,ops):
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)

# 测试示例
ops1 = ["5","-2","4","C","D","9","+","+"]
ops2 = ["1","C"]
s = Solution()
print(s.calPoints(ops2))