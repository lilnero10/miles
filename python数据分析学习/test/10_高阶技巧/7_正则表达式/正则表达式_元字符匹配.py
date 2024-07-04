import re

s = "lilnero @@python3 !!!666 #czy123"

# #"\d"只要数字
# result = re.findall(r'\d',s)  #字符串前带上r标记，表示字符串中转义字符无效，就是普通字符的意思
# print(result)
#
# result = re.findall(r'\W',s)
# print(result)
#
# result = re.findall(r'[a-zA-Z0-9]',s)
# print(result)

#匹配账号，只能由数字和字母组成，长度6-10位
r = '^[0-9a-zA-Z]{6,10}$' #规则 ^$从开头匹配到结尾
s = '123456780123'
print(re.findall(r, s))

#匹配QQ号，要求纯数字，长度5-11位，第一位不为0
x = '^[1-9][0-9]{4,10}$'
y = '2357577930'
print(re.findall(x, y))

#匹配邮箱地址，只允许qq,163,gmail的邮箱格式
#{内容}.{内容}.{内容}.{内容}@{内容}.{内容}
a = '^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$'
b = '2357577930@qq.com'
print(re.findall(a, b))