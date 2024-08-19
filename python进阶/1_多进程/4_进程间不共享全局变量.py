""""
创建子进程会对主进程资源进行拷贝，也就是说子进程是主进程的一个副本，好比是一对双胞胎，之所以进程之间不
共享全局变量，是因为操作的不是同一个进程里面的全局变量，只不过不同进程里面的全局变量名字相同而已
"""

import multiprocessing

my_list =[]
def write_data():
    for i in range(3):
        my_list.append(i)
        print("add:", i)
    print("write_data", my_list)

def read_data():
    print("read_data", my_list)

if __name__ == "__main__":
    #创建写入数据进程
    write_process = multiprocessing.Process(target=write_data)
    #创建读取数据进程
    read_process = multiprocessing.Process(target=read_data)
    # 启动进程执行相应任务
    write_process.start()
    read_process.start()