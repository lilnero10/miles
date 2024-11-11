"""
演示非单例模式效果
"""

class StrTools:
    pass

str1 = StrTools()
str2 = StrTools()
print(str1)
print(str2)
#str1和str2的地址信息不同