def func_outer(num1):
    def func_inner(num2):
        num3 = num1 + num2
    return func_inner

#创建闭包实例
f = func_outer(10)