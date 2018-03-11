# 要求：输入公交卡当前的余额，只要超过2元，就可以上公交车；
# 如果车上有空座位，就可以坐下。
import random                      # 导入random 模块
money = eval(input("所剩余额:"))   # eval用来计算在字符串中的有效Python表达式,并返回一个对象
if money >= 2:
    print("您可以上车")
    seat = random.randint(0, 1)    # 在0、1中随机产生一个数
    if seat == 1:
        print("有座位，您可以坐下")
    else:
        print("没座位了，您站着吧")
else:
    print("余额不足，您不可以上车")
