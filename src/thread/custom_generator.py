def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # 如果一个函数有yield语句，那么他就不再是函数，而是一个生成器模板
        ret = yield a
        print("...ret...", ret)
        a, b = b, a + b
        current_num += 1
    return "test..."


def main():
    nums = create_num(10)
    # for num in nums:
    #     print(num)
    # while True:
    #     try:
    #         ret = next(nums)
    #         print(ret)
    #     except Exception as e:
    #         print(e.value)
    #         break
    ret = next(nums)
    print(ret)
    ret = nums.send("hello")
    print(ret)


if __name__ == '__main__':
    main()
