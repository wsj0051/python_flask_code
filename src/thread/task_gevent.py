import time
import gevent
from gevent import monkey

monkey.patch_all()


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


# g1 = gevent.spawn(f1, 5)
# g2 = gevent.spawn(f2, 5)
# g3 = gevent.spawn(f3, 5)
# g1.join()
# g2.join()
# g3.join()
gevent.joinall([
    gevent.spawn(f1, 5),
    gevent.spawn(f2, 5),
    gevent.spawn(f3, 5)
])