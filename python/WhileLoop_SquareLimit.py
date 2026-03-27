# codin = utf-8
# 本程序通过 while 循环寻找平方小于 1000 的最大正整数，练习循环条件的边界判断”，文件名用MaxInt_LessThan1000_Square.py

i = 0

while i * i < 1000:
    i += 1

print ("i =", i)
print ("i * i =", i * i)