from multiprocessing import Pool, Manager
import os


def copy_file(q, file_name, o_dir, n_dir):
    old_f = open(o_dir + "\\" + file_name, "rb")
    content = old_f.read()
    old_f.close()
    new_f = open(n_dir + "\\" + file_name, "wb")
    new_f.write(content)
    new_f.close()
    q.put(file_name)


def main():
    # 1. 获取用户要拷贝的文件夹
    o_folder = "D:\\BaiduNetdiskDownload\\1-3 面向对象\\01-面向对象基础"
    n_folder = o_folder + "_bak"
    # 2. 创建一个新的文件夹
    try:
        os.mkdir(n_folder)
    except:
        pass
    dir_list = os.listdir(o_folder)
    po = Pool(3)
    q = Manager().Queue()
    for file_name in dir_list:
        po.apply_async(copy_file, args=(q, file_name, o_folder, n_folder))
    po.close()
    # po.join()
    all_file_num = len(dir_list)
    copy_ok = 0
    while True:
        file_name = q.get()
        copy_ok += 1
        print("\r已经完成copy:%s 进度 %.2f %%" % (file_name, copy_ok*100/all_file_num), end="")
        if copy_ok >= all_file_num:
            break
    print()

if __name__ == '__main__':
    main()
