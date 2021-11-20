class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s" %
                (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("添加家具：%s" % item)
        # 判断家具面积
        if item.area > self.free_area:
            print("%s 的面积太大了，无法添加" % item.name)
            return
        # 将加具名称添加到列表
        self.item_list.append(item.name)
        # 计算剩余面积
        self.free_area -= item.area


bed = HouseItem("床", 5)
chest = HouseItem("衣柜", 3)
table = HouseItem("桌子", 3)
soft = HouseItem("沙发", 10)

print(bed)
print(chest)
print(table)
home = House("两室一厅", 77)
home.add_item(bed)
home.add_item(chest)
home.add_item(table)
home.add_item(soft)
print(home)
