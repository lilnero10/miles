import json
#通过json.dumps(data)方法把python数据转化为json数据
#  data = json.dumps(data)
#如果有中文可以带上： ensure_ascii=False 参数来确保中文正常转换


#通过 json.loas(data)方法把json数据转化为python列表或字典
# data = json.loads(data)

#列表
data = [{"name":"czy","age":11},{"name":"qwe","age":12},{"name":"csd","age":11}]
json_str = json.dumps(data,ensure_ascii=False)
print(json_str)

#字典
d = {"name":"czy","addr":"上海市"}
json_str = json.dumps(d,ensure_ascii=False)
print(json_str)

#json字符串转换为Python数据类型
s = '[{"name":"czy","age":11},{"name":"qwe","age":12},{"name":"csd","age":11}]'
json = json.loads(s)
