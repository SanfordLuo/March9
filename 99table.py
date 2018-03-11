# 打印九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <=i:
        print("%d*%d=%-4d" % (j, i, j*i), end="")   # 加end=""是防止换行；%-4d左对齐占4格
        j += 1
    print()                     # 换行
    i += 1
