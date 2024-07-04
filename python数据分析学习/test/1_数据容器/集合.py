#集合不能重复，元素顺序不能保证
my_set = {"czy","123","q12","czy","123","q12","czy","123","q12"}
my_set_empty = set()
print(f"my_set的内容是：{my_set}")

#合并集合
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(set3)