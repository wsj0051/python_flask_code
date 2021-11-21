class Fibonacci(object):
    """自定义迭代器"""

    def __init__(self, all_num):
        self.all_nums = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_nums:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration


def main():
    fibo = Fibonacci(10)
    for num in fibo:
        print(num)
    # nums = list()
    # a = 0
    # b = 1
    # i = 0
    # while i < 10:
    #     nums.append(a)
    #     a, b = b, a+b
    #     i += 1
    #
    # for num in nums:
    #     print(num)


if __name__ == '__main__':
    main()
