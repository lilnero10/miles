from pyspark import SparkConf, SparkContext
import os
#链接pyspark到python解释器
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.12"
os.environ['HADOOP_HOME'] = "/Library/Frameworks/hadoop-3.3.6"
#创建sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")  #链式调用

#方式1，SparkConf对象设置全局并行度为1 #用于输出文件时为一个文件
conf.set("spark.default.parallelism", "1")

#基于sparkconf类对象创建sparkcontext类对象
sc = SparkContext(conf=conf)

file_rdd = sc.textFile("/Users/chenzhiyong/PycharmProjects/python数据分析学习/test/9_PySpark实战/data.txt")
# TODO 需求1:热门搜索时间段top3（小时精度）
# 1.1 取出全部时间并转换为小时
# 1.2 转换为（小时，1）二元元组
# 1.3 key分组聚合value
# 1.4 排序
# 1.5 取前三
#.map(lambda x: (x.split("\t")[0][:2],1)) #'\t'空格分隔 '[0][:2]'0号元素的前两个字符
result1 = file_rdd.map(lambda x: x.split("\t")).\
    map(lambda x: x[0][:2]).\
    map(lambda x: (x,1)).\
    reduceByKey(lambda x, y: x + y).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(3)

print("需求1的结果:",result1)

# TODO 需求2:将数据转换为json格式，写出到文件中
# 2.1 转换为json格式的RDD
# 2.2 写出为文件
file_rdd.map(lambda x: x.split()).\
        map(lambda x: {"time": x[0],"name": x[1],"search": x[2],"url": x[3]}).\
        saveAsTextFile("/Users/chenzhiyong/PycharmProjects/python数据分析学习/test/9_PySpark实战/output_json")
