import time
import threading

def work():
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)


if __name__ == "__main__":
    # 创建子进程
    work_thread = threading.Process(target=work)

    # 设置守护主线程方式1，daemon=True守护主线程
    # work_thread = threading.Thread(target=work, daemon=True)

    work_thread.start()
    # 让主进程等待1秒钟
    time.sleep(1)
    print("主进程执行完成了")