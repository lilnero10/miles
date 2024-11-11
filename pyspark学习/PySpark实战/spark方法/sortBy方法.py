from pyspark import SparkConf, SparkContext
import os
#链接pyspark到python解释器
os.environ['PYSPARK_PYTHON'] = "/usr/local/bin/python3.12"

#创建sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")  #链式调用

#基于sparkconf类对象创建sparkcontext类对象
sc = SparkContext(conf=conf)

#读取文件
rdd = sc.textFile("")  #单词文件路径
#提取单词
word_rdd = rdd.flatMap(lambda line: line.split())
#转换为二元元组
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
#分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a, b: a + b)


#根据元祖中第二个单词数量进行排序 #True从小到大，False从大到小 #全局排序设置分区数为1
final_rdd = result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)

print(final_rdd.collect())