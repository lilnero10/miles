my_list = [1,2,3,4,5,6,7,8]


def list_while_func():
    #循环控制变量通过下标索引来控制，默认0
    #每一次循环下标索引+1
    #循环条件：下标索引变量< 列表的元素数量

    #定义一个变量用来标记列表的下标
    index = 0   #初始值为0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表的元素:{element}")
        index += 1

def list_for_func():
    for element in my_list:
        print(f"列表的元素有：{element}")
