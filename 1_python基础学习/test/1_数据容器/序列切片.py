my_list= [0,1,2,3,4,5,6,7,8,9]
num1 = my_list[1:4:1]  #步长默认是1，可以省略不写
print(f"{num1}")


my_tuple= (0,1,2,3,4,5,6,7,8,9)
num2 = my_tuple[:]  # 起始结束不写表示从头到尾，步长默认是1，所以可以省略不写
print(f"{num2}")

my_str= (0,1,2,3,4,5,6,7,8,9)
num3 = my_str[::2]  # 步长为2
print(f"{num3}")

#反转序列
my_str= (0,1,2,3,4,5,6,7,8,9)
num4 = my_str[::-1]  # 步长为-1
print(f"{num4}")

#倒序切片
my_str= (0,1,2,3,4,5,6,7,8,9)
num5 = my_str[4:2:-1]  # 步长为-1
print(f"{num5}")

