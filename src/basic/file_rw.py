def file_read(dir):
    file = open(dir)
    text = file.read()
    print(text)
    file.close()


def file_write(dir):
    """
    r: 只读，默认模式
    w: 只写，文件存在会被覆盖
    a: 追加方式打开
    r+: 读写方式打开，指针在文件的开头
    w+: 读写方式，，文件会被覆盖
    a+: 指针在文件结尾

    """
    file = open(dir, "a")
    file.write("123")
    file.close()


def file_read_line(dir):
    file = open(dir)
    while True:
        text = file.readline()
        if not text:
            break
        print(text, end="")

    file.close()


def file_copy(dir):
    read = open(dir)
    write = open(dir + "bak", "w")
    text = read.read()
    write.write(text)
    read.close()
    write.close()


def file_copy_line():
    read = open(dir)
    write = open(dir + "bak", "w")
    while True:
        text = read.readline()
        if not text:
            break
        write.write(text)
    read.close()
    write.close()


if __name__ == '__main__':
    dir = "d:\\test.txt"
    # file_write(dir)
    # file_read(dir)
    # file_read_line(dir)
    # file_copy(dir)
    file_copy_line(dir)
