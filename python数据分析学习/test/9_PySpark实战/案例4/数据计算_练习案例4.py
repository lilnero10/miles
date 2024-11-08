# coding:utf-8

from pyspark import SparkConf, SparkContext
from pyspark.storagelevel import StorageLevel
from defs import context_jieba,filter_words,append_words,extract_user_and_word
from operator import add

if __name__ == '__main__':
    conf = SparkConf().setAppName("test").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    file_rdd = sc.textFile(" ../../data/input/SogouQ.txt")

    split_rdd = file_rdd.map(lambda x: x.split("\t"))

    # 3.因为要做多个需求，split_rdd作为基础的rdd会被多次使用.
    split_rdd.persist(StorageLevel.DISK_ONLY)

    # TODO 需求1:用户搜索的关键词分析
    context_rdd = split_rdd.map(lambda x: x[2])

    words_rdd = context_rdd.flatMap(context_jieba)

    filtered_rdd = words_rdd.filter(filter_words)

    filter_words_rdd = filtered_rdd.map(append_words)

    # 对单词进行 分组、聚合、排序、求前5
    # ascending=False,numPartitions=1（降序、全局有效）
    final_word_rdd = filter_words_rdd.reduceByKey(lambda a, b: a + b).\
        sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
        take(5)


    print('最热关键词、搜索次数',final_word_rdd)

    # TODO 需求2:用户和关键词组合分析
    user_content_rdd = split_rdd.map(lambda x: (x[1], x[2]))

    # 对用户的搜索内容进行分词，分词后和用户ID再次组合
    user_word_with_one_rdd = user_content_rdd.flatMap(extract_user_and_word)

    # 对单词进行 分组、聚合、排序、求前5
    # ascending=False,numPartitions=1（降序、全局有效）
    user_word_rdd = filter_words_rdd.reduceByKey(lambda a, b: a + b).\
        sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
        take(5)

    # TODO 需求3:热门搜索时间段分析
    time_rdd = split_rdd.map(lambda x: x[0])

    hour_rdd = time_rdd.map(lambda x: (x.split(":")[0], 1))

    # 分组、聚合、排序
    result3= hour_rdd.reduceByKey(add).sortBy(lambda x:x[1],ascending=False,numPartitions=1)