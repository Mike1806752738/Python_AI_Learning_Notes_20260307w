# coding = utf-8
# 代码文件: for_loop_statement_demo.py

print ("-----字符串------")
for item in "Hello":
    print(item)

# 声明整数列表
numbers = [43,32,55,74]  
print ("-----整数列表------")
for item in numbers:
    print(item)

# 取值 >= 0 且 < 10 的整数序列
print ("----->= 0 且 < 10整数列表------")
for item in range(10):
    print(item)
else:
    print("For Over!")

# break中断前0-9， 中断后0-2
print ("-----条件满足3时中断------")
for item in range(10):
    if item == 3:
        break
    print(item)
else:
    print("For Over!")