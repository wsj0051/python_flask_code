# 记录所有的名片字典
card_list = []


def show_menu():
    print("*" * 50)
    print("""欢迎使用【名片管理系统】V1.0""")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("0. 退出程序")
    print("*" * 50)


def add_card():
    """新增名片"""
    print("*" * 50)
    print("新增名片")
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ号：")
    email = input("请输入邮箱：")
    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email}
    card_list.append(card_dict)
    print("添加 %s 的名片信息成功！" % name)
    print(card_list)


def show_all():
    """显示所有名片"""
    print("*" * 50)
    print("显示所有名片")
    if len(card_list) == 0:
        print("当前没有名片记录，请添加名片！")
        return

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t\t")
    print("")
    print("=" * 50)
    for card_dict in card_list:
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],
                                              card_dict["phone"],
                                              card_dict["qq"],
                                              card_dict["email"]))


def find_card():
    """查询名片"""
    print("*" * 50)
    print("查询名片")
    find_name = input("请输入要查询的姓名：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("找到了")
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],
                                                  card_dict["phone"],
                                                  card_dict["qq"],
                                                  card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("没有找到 %s 的名片！" % find_name)


def deal_card(find_dict):
    action_str = input("请选择要执行的操作【1】.修改 【2】.删除 【0】.返回上级菜单")
    print("*" * 50)

    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")
        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功！")


def input_card_info(dict_value, name):
    name_str = input(name)
    if len(name_str.strip()) == 0:
        print("%s不修改" % name)
        return dict_value
    else:
        return name_str
