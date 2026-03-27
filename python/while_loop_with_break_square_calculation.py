# 带有 break 终止条件的 while 循环，计算变量 i 的平方值

i = 0

while i * i < 10:
    i += 1
    if i == 3:
        break
    print(str(i)+" * " + str(i)+" = ",i * i)
else:
    print("While over!")