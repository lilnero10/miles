#闭包ATM案例
#def atm闭包函数
def account_create(initial_amount=0):      #initial_amount只是作用于account_create函数内部的全局变量，
    def atm(num,deposit=True):             #内部atm函数依赖外部initial_amount变量，initial_amount变量为外部函数的内部临时变量
        nonlocal initial_amount            #外部变量持续不断的记录值，确保外部变量不是全局的，不会被篡改掉
        if deposit:
            initial_amount += num
            print(f"存款：+{num},账户余额：{initial_amount}")
        else:
            initial_amount -= num
            print(f"存款：-{num},账户余额：{initial_amount}")

    return atm()

atm=account_create()
atm(19999)


#修改闭包内使用的外部函数变量使用nonlocal关键字来完成
def func_outer(num1):
    def func_inner(num2):
        nonlocal num1
        num1 = num2 +20

    print(num1)
    func_inner(10)
    print(num1)
    return func_inner

#创建闭包实例
func_outer(10)