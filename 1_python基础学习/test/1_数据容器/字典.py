dict1 = {"王力宏":{"语文":88,"数学":87,"英语":89},
         "周杰伦":{"语文":88,"数学":87,"英语":89}}

score_stu = dict1["王力宏"]["语文"]
print(score_stu)

#获取全部keys
dict1 = {"王力宏":{"语文":88,"数学":87,"英语":89},
         "周杰伦":{"语文":88,"数学":87,"英语":89}}
keys = dict1.keys()

#遍历字典
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{dict1[key]}")

#统计字典内元素数量
num = len(dict1)
print(f"字典内元素数量有:{num}个")