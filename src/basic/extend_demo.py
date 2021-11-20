class Animal:
    def eat(self):
        print("吃...")

    def drink(self):
        print("喝...")

    def run(self):
        print("跑...")

    def sleep(self):
        print("睡...")


class Dog(Animal):
    def bark(self):
        print("汪汪叫。。。")


class Cat(Animal):
    def catch(self):
        print("抓老鼠。。。")


class XiaoTianQuan(Dog):
    def fly(self):
        print("飞...")

    def bark(self):
        print("可以说人话。。。")
        # super(XiaoTianQuan, self).bark()
        # Dog.bark(self)
        super().bark()


xtq = XiaoTianQuan()
xtq.sleep()
xtq.fly()
xtq.bark()
