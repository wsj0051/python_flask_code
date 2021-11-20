import time
import threading


def sing():
    for i in range(5):
        print("正在唱歌")
        time.sleep(1)


def dance():
    for i in range(5):
        print("正在跳舞")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


def say():
    print("hello world")
    time.sleep(1)


if __name__ == '__main__':
    # main()
    for i in range(5):
        t = threading.Thread(target=say)
        t.start()
