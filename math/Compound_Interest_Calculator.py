# 定义一个专门计算复利终值的函数
def calculate_compound_interest(principal, annual_rate, years):
    # 将输入的年利率（如 5%）转换为小数形式（0.05），方便数学计算
    rate_decimal = annual_rate / 100
    # 核心复利公式：F = P * (1 + i) ** n
    # principal 是本金 P，rate_decimal 是利率 i，years 是期数 n
    future_value = principal * (1 + rate_decimal) ** years
    # 将计算好的终值结果返回
    return future_value

# ------------------- 以下是代码使用示例 -------------------

# 设定初始本金（例如 10000 元）
initial_principal = 10000
# 设定年利率（例如 5%，这里只填数字 5）
yearly_rate = 5
# 设定投资/存款年数（例如 3 年）
investment_years = 3

# 调用上面定义的函数，传入三个参数，得到最终结果
final_amount = calculate_compound_interest(initial_principal, yearly_rate, investment_years)

# 打印结果，使用 :.2f 让结果保留两位小数，更符合金额显示习惯
print(f"复利终值为：{final_amount:.2f} 元")
