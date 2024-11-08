from pyspark import SparkContext, SparkConf
"""
使用场景：本地集合对象 和 分布式集合对象（RDD）进行关联的时候，适用于小数据量场景
需要将本地集合对象封装为广播变量
可以节省：
1、网络IO的次数
2、executor内存占用
"""

if __name__ == '__main__':

    # 配置 Spark
    conf = SparkConf().setAppName("LogIDCount").setMaster("local")
    sc = SparkContext(conf=conf)

    stu_info_list = [(1,'张大',11),
                      (2,'李四',13),
                      (3,'王五',11),
                      (4,'赵六',11),]
    # 1、将本地pythonlist对象标记为广播变量
    broadcast = sc.broadcast(stu_info_list)

    score_info_rdd = sc.parallelize([(1, '语文', 99),
                                     (2, '数学', 99),
                                     (3, '英语', 99),
                                     (4, '编程', 99),
                                     (1, '语文', 99),
                                     (2, '数学', 99),
                                     (3, '英语', 99),
                                     (4, '编程', 99),
                                     (1, '语文', 99),
                                     (2, '数学', 99),
                                     (3, '英语', 99),
                                     (4, '编程', 99),
                                     ])
    def map_func (data):
        id = data[0]
        name = ""
        # 匹配本地list和分布式RDD中的学生ID 匹配成功后，即可获得当前学生的姓名
        # 2、在使用到本地集合变量的地方，从广播变量取出来用即可
        for stu_info in broadcast.value:
            stu_id = stu_info[0]
            if id == stu_id:
                name = stu_info[1]
        return (name,data[1],data[2])

    print(score_info_rdd.map(map_func).collect())
