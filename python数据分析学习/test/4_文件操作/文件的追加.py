#打开文件
f = open("/Users/czy/demo.txt","a", encoding="UTF-8")
#"a"模式，文件不存在会创建文件，文件存在会在最后追加写入

#文件写入
f.write('hello world')

#内容刷新
f.flush()
