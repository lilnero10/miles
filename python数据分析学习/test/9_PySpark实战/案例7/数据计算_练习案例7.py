from pyspark import SparkContext, SparkConf
import re
if __name__ == '__main__':

    # 配置 Spark
    conf = SparkConf().setAppName("LogIDCount").setMaster("local")
    sc = SparkContext(conf=conf)

    file_rdd = sc.textFile("/Users/chenzhiyong/PycharmProjects/lilnero/python数据分析学习/test/9_PySpark实战/案例7/logdata.txt")

    abnormal_char = [',','.','#','!','$','%']

    # 2、将特殊字符list包装成广播变量
    broadcast = sc.broadcast(abnormal_char)

    # 3、对特殊字符出现次数做累加，使用累加器最好
    acmlt = sc.accumulator(0)

    # 先处理数据的空行
    lines_rdd = file_rdd.filter(lambda x:x.strip())
    # 处理行内空行
    data_rdd = lines_rdd.filter(lambda x:x.strip())
    # 处理空格
    words_rdd = data_rdd.flatMap(lambda x: re.split("\s+",x))

    # 过滤正常单词和特殊符号
    def filter_func(data):
        global acmlt

        abnormal_char = broadcast.value

        if data in abnormal_char:
            acmlt += 1
            return True
        else:
            return False

    normal_words_rdd = words_rdd.filter(filter_func)

    number_words_rdd = normal_words_rdd.map(lambda x:(x,1)).reduceByKey(lambda a, b: a + b)

    print(f"单词个数：{number_words_rdd.collect()}")
    print(f"特殊符号个数：{acmlt}")




