from pyspark import SparkConf, SparkContext
import os
# 链接pyspark到python解释器
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.12"
os.environ['HADOOP_HOME'] = "/Library/Frameworks/hadoop-3.3.6"
# 创建sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")  # 链式调用

# 方式1，SparkConf对象设置全局并行度为1 #用于输出文件时为一个文件
conf.set("spark.default.parallelism", "1")

# 基于sparkconf类对象创建sparkcontext类对象
sc = SparkContext(conf=conf)

# 方式2，创建RDD时设置全局并行度
# rdd = sc.parallelize([1,2,3,4,5,6],numSlices=1) #数据容器对象
# rdd = sc.parallelize([1,2,3,4,5,6],1)

# 创建RDD对象
rdd = sc.parallelize([1,2,3,4,5,6])


# #通过textfile方法，把文件内容加载到Spark中，成为RDD对象
# rdd = sc.textFile("file:")  #文件路径

# 自定义方法
# def func(data):
#     return data * 100

# rdd1 = rdd.map(func)

# #匿名函数方法
# rdd1 = rdd.map(lambda x: x * 10)

# 输出到文件中
rdd.saveAsTextFile("/Users/chenzhiyong/Downloads/output1")

# 停止sparkcontext对象的运行（停止pyspark程序）
# sc.stop()