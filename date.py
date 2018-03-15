print("----2.1 判断有效日期----")
while True:
    date = input("请输入日期(yyyymmdd)：")
    if not date.isdigit() or len(date) != 8 :
        print("输入的内容必须都是数字且为8位数,请重新输入")
        continue
    else:
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:])
        big_month = [1, 3, 5, 7, 8, 10, 12]
        small_month = [4, 6, 9, 11]

        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):   # 闰年
                if day < 1 or day > 29:
                    print("无效的日期，闰年2月的天数是1~29")
            else:
                if day < 1 or day > 28:
                    print("无效的日期，普通2月的天数是1~28")
        elif month < 1 or month > 12:
            print("无效的日期，月份为1~12")
        elif (month in big_month) and (day < 1 or day > 31):
            print("无效的日期，这个月的天数是1~31")
        elif (month in small_month) and (day < 1 or day > 30):
            print("无效的日期，这个月的天数是1~30")
        else:
            print("有效的日期")
        break
