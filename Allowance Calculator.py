Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> daily_money = input("请输入每天存的零花钱（单位：元）：")
请输入每天存的零花钱（单位：元）：10
>>> days = input ("请输入存钱的天数：")
请输入存钱的天数：30
>>> 
>>> daily_money = float(daily_money)
>>> days = int(days)
>>> total = daily_money * days
>>> print ("总零花钱为：", total)
总零花钱为： 300.0
