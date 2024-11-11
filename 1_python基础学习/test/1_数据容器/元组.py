#元组内元素不可修改
t1 = ((1,2,3),(4,5,6))
num = t1[1][2]
print(f"从嵌套元组中取出数据是：{num}")

#index方法
t2 = (1,2,3,4,5,6)
index = t2.index(4)
print(f"从t2元组中取出数据的下标是：{index}")

#count方法
t3 = (1,2,2,2,2,2,4)
num = t3.count(2)
print(f"统计t3元祖中2的数量有：{num}个")