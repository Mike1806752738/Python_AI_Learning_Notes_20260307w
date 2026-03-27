import numpy as np  
import matplotlib.pyplot as plt  

# ========== 【唯一配置区】你只改这里！ ==========
# 1. 一次函数参数列表（想加几条加几条，删/注释即可控制数量）
# 格式：[(斜率k, 截距b, 颜色, 线条样式), ...]
# 线条样式：'-'实线 | '--'虚线 | ':'点线 | '-.'点划线
LINE_PARAMS = [
    (3, -2, 'blue', '-'),    # 第1条：y=3x-2（蓝色实线）
    (-2, 3, 'red', '--'),    # 第2条：y=-2x+3（红色虚线）
    (1, -1, 'green', ':'),   # 第3条：y=x-1（绿色点线，注释则隐藏）
    # (0, 5, 'orange', '-.'),  # 第4条：y=5（橙色点划线，按需启用/注释）
]

# 2. 功能开关（True显示 / False隐藏）
SHOW_CROSS_POINTS = True  # 显示直线交点（多条线时生效）
SHOW_FUNCTION_LABEL = True# 显示函数公式标注
SHOW_GRID = False         # 显示网格

# ========== 【核心逻辑区】无需修改 ==========
# 全局样式配置（解决中文/负号显示）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.linewidth'] = 0.8

# 初始化画布和坐标轴（课本风格十字轴）
fig, ax = plt.subplots(figsize=(8, 6))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 坐标轴小箭头
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, linewidth=0.8, markersize=3)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, linewidth=0.8, markersize=3)

# 坐标轴标签
ax.set_xlabel('x轴', fontsize=10, loc='right', labelpad=5)
ax.set_ylabel('y轴', fontsize=10, loc='top', rotation=0, labelpad=10)

# 定义x轴范围（-10到10，保证线条平滑）
x = np.linspace(-10, 10, 200)
ax.set_xticks(np.arange(-10, 11, 2))
ax.set_yticks(np.arange(-20, 31, 2))

# 批量绘制一次函数直线 + 公式标注
label_x_positions = [8, -8, 6, -6, 4, -4]  # 公式标注x位置（自动错开）
for idx, (k, b, color, style) in enumerate(LINE_PARAMS):
    # 计算y值
    y = k * x + b
    # 绘制直线
    ax.plot(x, y, color=color, linestyle=style, linewidth=1.5)
    
    # 函数公式标注（开关控制 + 自动错开）
    if SHOW_FUNCTION_LABEL:
        label_x = label_x_positions[idx % len(label_x_positions)]
        label_x_idx = np.argmin(np.abs(x - label_x))  # 找最接近的x索引
        label_y = y[label_x_idx] + 1.2  # y轴偏移避免重叠
        # 拼接公式（处理b的正负）
        func_label = f'y = {k}x + {b}' if b >= 0 else f'y = {k}x - {abs(b)}'
        ax.text(label_x, label_y, func_label, fontsize=10, color=color,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

# 批量计算并标注所有两两直线的交点（开关控制 + 多条线生效）
if SHOW_CROSS_POINTS and len(LINE_PARAMS) >= 2:
    for i in range(len(LINE_PARAMS)):
        k1, b1, _, _ = LINE_PARAMS[i]
        for j in range(i + 1, len(LINE_PARAMS)):  # 只算i<j，避免重复计算
            k2, b2, _, _ = LINE_PARAMS[j]
            if k1 != k2:  # 斜率不同才有交点
                cross_x = (b2 - b1) / (k1 - k2)
                cross_y = k1 * cross_x + b1
                # 绘制交点圆点
                ax.plot(cross_x, cross_y, 'ko', markersize=5)
                # 标注交点坐标
                ax.text(cross_x + 0.3, cross_y + 0.3, f'({cross_x:.1f}, {cross_y:.1f})',
                        fontsize=8, bbox=dict(boxstyle='round,pad=0.2', facecolor='yellow', alpha=0.7))

# 显示网格（开关控制）
if SHOW_GRID:
    ax.grid(True, linestyle='--', alpha=0.3)

# 调整布局避免标签截断
plt.tight_layout()
# 显示图像
plt.show()