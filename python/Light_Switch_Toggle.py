# 任务2：模拟灯泡开关切换
# 提示用户输入灯泡当前状态（0：关，1：开）state 状态 input 输入
state = input ("请输入灯泡当前状态（0代表关，1代表开）：")

# 将输入的字符串转换为整数
state = int(state)

# 使用异或运算符^切换状态（0变1，1变0）
new_state = state ^ 1

# 输出切换后的灯泡状态
print("切换后的灯泡状态是：", new_state)
