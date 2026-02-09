from add import add_nums
from sub import sub_nums
from multiply import multiply_nums
from divide import divide_nums

def start():
    ishora = ['+','+','*','//']
    while True:
        x = int(input("1-son (0 to stop): "))
        if x == 0:
            break
        y = int(input("2-son: "))
        amal = input(f"{ishora}lardan tanlang: ")
        if not amal in ishora:
            print(f"Xato amal faqat {sihora}")
            continue
        if amal == '+':
            print(add_nums(x,y))
        elif amal == '-':
            print(sub_nums(x,y))
        elif amal == '*':
            print(multiply_nums(x,y))
        else:
            print(divide_nums(x,y))
start()