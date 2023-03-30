
def askforInt():
    while True:
        num = input("please enter num: ")
        if num.isdigit():
            return int(num)
        print("----- please enter valid number ----")