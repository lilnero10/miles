import threading
import time

my_list = []
def write_data():
    for i in range(10):
        print("add:",i)
        my_list.append(i)
    print("write:",my_list)

def read_data():
    print("read:",my_list)

if __name__ == "__main__":
    #创建子进程
    writre_thread = threading.Thread(target=write_data)
    read_thread = threading.Thread(target=read_data)

    #启动进程
    writre_thread.start()
    #延迟1秒
    time.sleep(1)
    read_thread.start()

