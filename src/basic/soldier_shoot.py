class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count > 0:
            print("[%s]发射子弹。。biu biu" % self.model)
            self.bullet_count -= 1
        else:
            print("[%s]没有子弹" % self.model)


class Solider:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        # 判断士兵是否有枪
        if self.gun is None:
            print("%s还没有枪" % self.name)
            return
        # 装子弹
        self.gun.add_bullet(50)
        # 射击
        self.gun.shoot()


ak47 = Gun("AK47")
xusanduo = Solider("许三多")
xusanduo.gun = ak47
xusanduo.fire()
