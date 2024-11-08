def generator(num):
    for i in range(num):
        print("开始")
        yield i #到这里暂停,方便记录代码执行状态
        print("生成完成")

g = generator(5)
print(next(g))