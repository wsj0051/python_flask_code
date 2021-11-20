def sum_number(num):
    if num == 1:
        return 1
    temp = sum_number(num - 1)
    return num + temp


print(sum_number(322))


# def sum_nums(args):
def sum_nums(*args):
    result = 0
    for num in args:
        result += num
    return result


# print(sum_nums((1, 2, 3, 4, 5)))
print(sum_nums(1, 2, 3, 4, 5))


def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_nums = (1, 2, 3)
gl_dict = {"name": "xiaoming", "age": 18}
# demo(gl_nums, gl_dict)
demo(*gl_nums, **gl_dict)
