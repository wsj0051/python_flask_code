from multiprocessing import Queue, Process


def download_from_web(q):
    data = [11, 12, 13, 14]
    for temp in data:
        q.put(temp)
    print("下载之后放入队列")


def analysis_data(q):
    waiting_analysis_data = list()
    while True:
        data = q.get()
        waiting_analysis_data.append(data)
        if q.empty():
            break

    print(waiting_analysis_data)


def main():
    q = Queue(3)
    p1 = Process(target=download_from_web, args=(q,))
    p2 = Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
