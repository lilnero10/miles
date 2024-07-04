import json
from pyspark import SparkConf, SparkContext
import os
#链接pyspark到python解释器
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.12"

#创建sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")  #链式调用

#基于sparkconf类对象创建sparkcontext类对象
sc = SparkContext(conf=conf)

#需求1：城市销售额排名
#读取文件
file_rdd = sc.textFile("")
#取出json字符串
json_rdd = file_rdd.flatMap(lambda line: line.split("|"))  #json文件中“|”分割
#将json字符串转为字典
dict_rdd = json_rdd.map(lambda x: json.loads(x))
#取出城市和销售额数据 #(城市，销售额）
data_rdd = dict_rdd.map(lambda x: (x['areaName'], x['money']))  #areaName、money是字典里的key
#按城市分组按销售额聚合
city_money_rdd = data_rdd.reduceByKey(lambda a,b: a + b)
#按销售额聚合结果进行排序
result_rdd = city_money_rdd.sortBy(lambda x: x[1], ascending=False)

print("需求1的结果:",result_rdd.collect())
#需求2:全部城市有哪些商品在售卖
#