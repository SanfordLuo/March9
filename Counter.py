# 设计简易计算器，可以进行基本的加减乘除运算
num1 = float(input("输入第一个数:"))
n = input("输入运算符(+ - * /):")
num2 = float(input("输入第二个数:"))

if n == "+":
    print("%.2f %s %.2f = %.2f" % (num1, n, num2, num1 + num2))
elif n == "-":
    print("%.2f %s %.2f = %.2f" % (num1, n, num2, num1 - num2))
elif n == "*":
    print("%.2f %s %.2f = %.2f" % (num1, n, num2, num1 * num2))
elif n == "/":
    print("%.2f %s %.2f = %.2f" % (num1, n, num2, num1 / num2))
