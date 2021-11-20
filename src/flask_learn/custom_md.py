def multiple_table():
    """9*9乘法表"""
    i = 1
    j = 1
    while i <= 9:
        # 在默认情况下，print函数输出以后，会自动在末尾增加换行
        j = 1
        while j <= i:
            print("%d * %d = %d" % (j, i, i * j), end="\t")
            j += 1
        print("")
        i += 1


def say_hello():
    print("hello 1")
    print("hello 12")
    print("hello 13")


def sum_num(a, b):
    return a + b