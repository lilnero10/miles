mylist = ["czy","qwe","abc"]

#修改特定下标索引的值
mylist[0] = "asd"
print(f"列表修改后，结果：{mylist}")

#在指定下标位置插入
mylist.insert(1,"wer")
print(f"列表插入后，结果：{mylist}")

#在列表尾部追加“单个”元素
mylist.append("nmd")
print(f"列表追加后，结果：{mylist}")

#在列表尾部追加列表
mylist.extend(["qaz","wsx","edc"])
print(mylist)

#删除
del mylist[2]
print(mylist)

#指定下标取出返回
element = mylist.pop(2)

#删除都一个匹配项
mylist.remove("czy")
print(mylist)

#清空列表
mylist.clear()

#统计匹配项
mylist.count("czy")

#统计列表总共元素数
print(len(mylist))