class Solution(object):
    def pow(self, x, n):
        num = pow(x,n)
        return num

    # 递归实现
    def pow_recursive(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.pow_recursive(x, -n)
        elif n % 2 == 0:
            half = self.pow_recursive(x, n // 2)
            return half * half
        else:
            return x * self.pow_recursive(x, n - 1)

    # 迭代实现
    def pow_iterative(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result


x = -3
n = -5
print(Solution().pow_iterative(x,n))