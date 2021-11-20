class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "%s 的体重是 %.1f" % (self.name, self.weight)

    def run(self):
        print("%s 开始跑步减肥。。" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 开始吃东西 " % self.name)
        self.weight += 1


xiaomi = Person("xiaomi", 75)
print(xiaomi.run())
print(xiaomi.eat())
print(xiaomi)
