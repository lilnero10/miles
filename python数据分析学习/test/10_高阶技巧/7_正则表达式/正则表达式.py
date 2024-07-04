"""
通过规则匹配字符串
"""
import re

#match 从头匹配
s = "python lilnero"
result = re.match("python",s)
print(result)
# print(result.span())
# print(result.group())

#search 搜索匹配
result = re.search("python", s)
print(result)

#findall 搜索全部匹配 使用最多
result = re.findall("python",s)
print(result)
