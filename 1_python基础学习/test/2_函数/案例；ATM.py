money = 5000000
name = None

name = input("请输入您的姓名：")

def query(show_header):
    if show_header:
       print("----------查询余额-----------")
    print(f"{name},您好，您的余额剩余：{money}元")


def saving(num):
    global money #money在函数内部定义为全局变量
    money += num
    print("-----------存款-------------")
    print(f"{name},您好，您存款{num}元成功。")

    query(False)#调用query查询余额

def get_money(num):
    global money #money在函数内部定义为全局变量
    money -= num
    print("-----------取款-------------")
    print(f"{name},您好，您取款{num}元成功。")

    query(False)  # 调用query查询余额

def main():
    print("----------主菜单------------")
    print(f"{name},您好，欢迎来到银行。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t[输入2]")
    print("取款\t[输入3]")
    print("退出\t[输入4]")
    return input("请输入您的选择：")

#设置无限循环，确保程序不退出
while True:
    keyword_input = main()
    if keyword_input == "1":
        query(True)
        continue  #通过continue继续下一次循环，一进来就回到了主菜单
    elif keyword_input == "2":
        num = int(input("您想要存多少钱？请输入："))
        saving(num)
        continue
    elif keyword_input == "3":
        num = int(input("您想要取多少钱？请输入："))
        get_money(num)
        continue
    else:
        print("退出")
        break

