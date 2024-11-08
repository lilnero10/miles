from pyspark import SparkContext, SparkConf
from defs import extract_id,parse_log_line


if __name__ == '__main__':

    # 配置 Spark
    conf = SparkConf().setAppName("LogIDCount").setMaster("local")
    sc = SparkContext(conf=conf)

    # 模拟加载日志数据
    log_data = sc.textFile("/Users/chenzhiyong/PycharmProjects/lilnero/python数据分析学习/test/9_PySpark实战/案例4/log.txt")

    # 创建 RDD
    log_rdd = sc.parallelize(log_data)

    # TODO 需求1:计算当前网站被访问次数
    # 解析日志并计算访问次数
    parsed_logs = log_rdd.map(parse_log_line)
    total_visits = parsed_logs.count()

    # TODO 需求2:计算当前访问的ID数量
    # 计算唯一的 ID 数量
    id_rdd = log_rdd.map(extract_id)
    unique_id_count = id_rdd.distinct().count()

    # 打印唯一 ID 的数量
    print(f"访问唯一ID数量: {unique_id_count}")
    # 打印总访问次数
    print(f"总访问次数: {total_visits}")

    # 关闭 Spark Context
    sc.stop()