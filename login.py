# 编写代码模拟用户登陆。
# 要求：用户名为 SanfordLuo，密码 123456，
# 如果输入正确，打印“欢迎光临”，程序结束，
# 如果输入错误，提示用户输入错误并重新输入
# 如果错误3次也将结束程序
real_name = "SanfordLuo"
real_password = "123456"
i = 1
while i <= 3:
    name = input("请输入用户名：")
    password = input("请输入密码：")
    if name == real_name and password == real_password:
        print("输入正确，欢迎光临")
        break
    else:
        print("第%d次输入错误，" % i + "您还剩%d次机会" % (3 - i))
    i += 1
print("-------程序结束-------")
