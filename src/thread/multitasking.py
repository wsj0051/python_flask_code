import time
import threading

g_nums = 1

mutex = threading.Lock()


def test1(num):
    global g_nums
    for i in range(num):
        mutex.acquire()
        g_nums += i
        mutex.release()
    print("--test1--g_nums=%s--" % str(g_nums))


def test2(num):
    global g_nums
    for i in range(num):
        mutex.acquire()
        g_nums += i
        mutex.release()
    print("--test2--g_nums=%s--" % str(g_nums))


def main():
    t1 = threading.Thread(target=test1, args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))
    t1.start()
    t2.start()
    print("--main--%s--" % str(g_nums))


if __name__ == '__main__':
    main()
