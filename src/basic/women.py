class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")
xiaofang._Women__secret()
print(xiaofang._Women__age)
"""
私有属性和方法在对象外不能被访问
用__下划线就会变成私有方法或属性
处理方式：_类名 => _类名__名称
"""