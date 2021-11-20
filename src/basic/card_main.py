import cards_tools


def welcome():
    while True:
        cards_tools.show_menu()
        action_str = input("请输入要执行的操作:")
        print("您选择的操作是【%s】" % action_str)
        # 1,2,3
        # 0 退出
        if action_str in ["1", "2", "3"]:
            if action_str == "1":
                cards_tools.add_card()
            elif action_str == "2":
                cards_tools.show_all()
            elif action_str == "3":
                cards_tools.find_card()
        elif action_str == "0":
            break
        else:
            print("您输入的操作不正确，请重新输入！")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    welcome()
