from pyspark import SparkConf, SparkContext
import os
#链接pyspark到python解释器
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.12"

#创建sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")  #链式调用

#基于sparkconf类对象创建sparkcontext类对象
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,2,3,4,5,6]) #数据容器对象

#自定义方法
def func(data):
    return data * 100

rdd1 = rdd.map(func)

# #匿名函数方法
# rdd1 = rdd.map(lambda x: x * 10)

#查看RDD里有什么内容
print(rdd1.collect())

