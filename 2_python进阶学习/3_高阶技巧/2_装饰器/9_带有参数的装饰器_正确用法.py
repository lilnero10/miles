def logging(flag):
    def decorator(fn):
        def inner(num1,num2):
            if flag == "+":
                print("正在加法计算中")
            elif flag == "-":
                print("正在减法计算中")
            result = fn(num1,num2)
            return result
        return inner
    return decorator

@logging('+')
def add(a,b):
    result = a + b
    return result

result = add(1,3)
print(result)