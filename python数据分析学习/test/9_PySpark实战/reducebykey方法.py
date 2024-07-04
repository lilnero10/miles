"""
分组并求和
"""
from pyspark import SparkConf, SparkContext
import os
#链接pyspark到python解释器
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.12"

#创建sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")  #链式调用

#基于sparkconf类对象创建sparkcontext类对象
sc = SparkContext(conf=conf)

rdd = sc.parallelize([('男',99),('男',88),('女',77),('女',66)])

rdd1 = rdd.reduceByKey(lambda a,b : a+b)

print(rdd1.collect())