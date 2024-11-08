"""
接收一个处理函数，可用lambda快速编写
对rdd逐个处理，得到ture的保留至返回值的RDD中
"""

from pyspark import SparkConf, SparkContext
import os
#链接pyspark到python解释器
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.12"

#创建sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")  #链式调用

#基于sparkconf类对象创建sparkcontext类对象
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,2,3,4,5])

rdd1 = rdd.filter(lambda x:x%2==0)

print(rdd1.collect())
