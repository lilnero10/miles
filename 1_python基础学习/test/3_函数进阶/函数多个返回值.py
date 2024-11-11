def test_return():
    return 1,2

x, y =test_return()
print(x)
print(y)


#函数作为参数传入
def func(compute):
    num = compute(1,2)
    print(num)

def compute(x,y):
    return x + y

#匿名函数
func(lambda x, y: x + y)