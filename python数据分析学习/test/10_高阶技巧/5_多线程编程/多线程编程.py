import time
import threading

def sing(msg):
    while True:   #每个线程持续工作
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    # 创建一个唱歌线程
    sing_thread = threading.Thread(target=sing,args=("唱歌ing",))  # 元组
    # 创建一个跳舞线程
    dance_thread = threading.Thread(target=dance,Kwargs={"msg": "跳舞ing"})  # 字典，key，value

    #启动线程
    sing_thread.start()
    dance_thread.start()
