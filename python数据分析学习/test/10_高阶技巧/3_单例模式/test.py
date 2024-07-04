"""
单例模式就是对一个类，只获取其唯一的类实例对象，持续复用它。
•节省内存
•节省创建对象的开销
"""

from str_tools import StrTools

s1 = StrTools
s2 = StrTools

print(id(s1))
print(id(s2))