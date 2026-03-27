score = int (input("请输入一个0~100的整数:"))

if score >= 60:
    if score >= 85:
        print("您真优秀")
    else:
        print("您真很好")
else:
    print("您需要努力")