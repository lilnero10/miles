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
