#打开文件
f = open("/Users/czy/demo.txt","r", encoding="UTF-8")

#读取文件
print(f.read(10))

#读取文件全部行，封装到列表里
lines = f.readlines()
print(lines)

#一次读取一行
line = f.readline()
print(line)

#for循环读取
for line in open("/Users/czy/demo.txt","r"):
    print(line)

#关闭文件
f.close()
