import time
import threading


def test1():
    """如果创建Thread时执行的函数运行结束，那么意味着这个子线程结束了"""
    for i in range(5):
        print("---test1--- %d" % i)
        time.sleep(1)


def test2():
    for i in range(5):
        print("---test2--- %d" % i)
        time.sleep(1)


def main():
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)
    print(threading.enumerate())

    # t2 = threading.Thread(target=test2)
    t1.start()
    # t2.start()
    print(threading.enumerate())

    # while True:
    #     if len(threading.enumerate()) == 1:
    #         break
    #     print(threading.enumerate())
    #     time.sleep(1)


if __name__ == '__main__':
    main()
