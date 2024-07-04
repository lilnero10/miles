#打开文件
f = open("/Users/czy/demo.txt","w", encoding="UTF-8")

#文件写入
f.write('hello world') #内容写入到了内存中

#内容刷新
f.flush() #将内存中的内容刷新到文件中

#关闭文件
f.close()
