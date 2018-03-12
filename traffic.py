# 依次输入是否为学生票、交通工具、里程
people = int(input("是否为学生：是(1) 否(0):"))
way = int(input("请选择交通方式：公交(1).地铁(0):"))
km = eval(input("请输入里程（km）："))
# 判断交通方式，是公交还是地铁
if way == 1:
    # 公交每次的原价为b_money
    # 公交总费用为b_total_money
    if km - 10 <= 0:
        b_money = 2
    else:
        b_money = 2 + (km - 10) // 5 + 1
    # 判断是否为学生票，进行折扣优惠
    if people == 1:
        b_total_money = 0.25 * b_money * 20 * 2
    else:
        b_total_money = 0.5 * b_money * 20 * 2
    print("每月乘坐公交需要的总费用:%d" % b_total_money)
else:
    # 地铁每次的原价s_money
    if km - 6 <= 0:
        s_money = 3
    elif km <= 12:
        s_money = 4
    elif km <= 22:
        s_money = 5
    elif km <= 32:
        s_money = 6
    else:
        s_money = 6 + (km - 32) // 20 + 1
    # 地铁的总费用s_total_money
    i = 1
    s_total_money = 0
    while i <= 20*2:
        if s_total_money <= 100:
            s_total_money += s_money
        elif s_total_money <= 150:
            s_total_money += s_money * 0.8
        elif s_total_money <= 400:
            s_total_money += s_money * 0.5
        else:
            s_total_money += s_money
        i += 1
    print("每月乘坐地铁需要的总费用:%d" % s_total_money)
