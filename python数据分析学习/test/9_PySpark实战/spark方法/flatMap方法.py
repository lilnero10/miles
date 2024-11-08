"""
flatmap算子和map算子功能相同
多了一层解除嵌套的功能
"""
from pyspark import SparkConf, SparkContext
import os
#链接pyspark到python解释器
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.12"

#创建sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")  #链式调用

#基于sparkconf类对象创建sparkcontext类对象
sc = SparkContext(conf=conf)

rdd = sc.parallelize("czy 123 qwe","czy 456 asd","czy 789 zxc") #数据容器对象

rdd1 = rdd.flatMap(lambda x: x.split(" "))

print(rdd1.collect())