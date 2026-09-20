from collections import Counter

import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 20


def frequency_bar_chart(data, value_range=(0, 100), title='频数柱状图'):
    """
    统计整数列表中每个值的出现次数, 并绘制柱状图

    参数:
        data: 整数列表, 如 [55, 56, 70, 55]
        value_range: 横轴显示范围, 默认 (0, 100)
        title: 图表标题
    """
    if not data:
        print("数据为空")
        return

    # 1. 统计每个值出现的次数
    counts = Counter(data)
    values = sorted(counts.keys())  # 出现过的数值, 升序
    freqs = [counts[v] for v in values]  # 对应的频数

    # 2. 如果数据超出默认范围, 自动扩展
    lo = min(min(data), value_range[0])
    hi = max(max(data), value_range[1])

    # 3. 中文字体设置
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots(figsize=(12, 5))

    # 4. 画柱子: 宽度为 1, 表示每个柱子代表一个整数值
    bars = ax.bar(values, freqs, width=1.0,
                  color='steelblue', edgecolor='white')

    # # 5. 在柱子上方标注频数
    # for v, f in zip(values, freqs):
    #     ax.text(v, f, str(f), ha='center', va='bottom', fontsize=10)

    # 6. 坐标轴设置
    ax.set_xlim(lo, hi)  # 横轴固定 0~100
    ax.set_ylim(0, max(freqs) + 30)  # 纵轴留一点空间
    ax.set_xticks(range(lo, hi + 1, 5))  # 每 10 显示一个刻度
    ax.set_xlabel('数值')
    ax.set_ylabel('人数')
    ax.set_title(title, fontsize=14)
    ax.grid(axis='y', linestyle='--', alpha=0.4)

    plt.tight_layout()
    plt.show()


import matplotlib.pyplot as plt


def plot_bar_with_percent(data, title='操作题', ylabel='正确率'):
    """
    给定二元列表, 画柱状图, 柱顶标注数值 + 百分号

    参数:
        data: 二维列表, 每个子列表为 [字符串, 数值]
              例如 [['A', 30], ['B', 25.5], ['C', 44.5]]
        title: 图表标题
        ylabel: 纵轴名称
    """
    if not data:
        print("数据为空")
        return

    # 1. 拆出标签和数值 (保持原有顺序)
    labels = [str(item[0]) for item in data]
    values = [item[1] for item in data]

    # 2. 中文字体 + 全局字号
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.size'] = 13
    plt.rcParams['axes.titlesize'] = 18
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['xtick.labelsize'] = 13
    plt.rcParams['ytick.labelsize'] = 13

    # 3. 画布: 加宽, 留白更多
    fig, ax = plt.subplots(figsize=(11, 6))

    # 4. 柱子: 渐变感 + 圆角边框
    bars = ax.bar(labels, values,
                  color='#4C8CBF',          # 更柔和的蓝
                  edgecolor='white',
                  linewidth=1.2,
                  width=0.6,
                  zorder=3)                  # 让柱子盖住网格

    # 5. 柱顶标注: 更大更醒目
    for bar, val in zip(bars, values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2,
                height + max(values) * 0.015,   # 稍微抬高一点
                f'{val}%',
                ha='center', va='bottom',
                fontsize=13, fontweight='bold',
                color='#2C3E50')

    # 6. 标题: 加粗 + 与图留间距
    ax.set_title(title, fontsize=18, fontweight='bold',
                 color='#2C3E50', pad=18)

    # 7. 纵轴名称
    ax.set_ylabel(ylabel, fontsize=14, color='#2C3E50')

    # 8. 网格: 只留横向虚线, 更淡
    ax.grid(axis='y', linestyle='--', alpha=0.35, zorder=0)
    ax.set_axisbelow(True)

    # 9. 去掉上边框和右边框 (更现代)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')

    # 10. 纵轴留白
    ax.set_ylim(0, max(values) * 1.18)

    # 11. 去掉刻度线, 保留标签
    ax.tick_params(axis='both', length=0, colors='#2C3E50')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # data = [int(item[7]) for item in
    #         read_xlsx_to_list(file_path=fr"2026.09.15 - 25学年第二学期数据源/七年级汇总表.xlsx")[1:]]
    # frequency_bar_chart(data, value_range=(0, 100), title='数据分布')

    data_1 = ["第一题", 66.82],["第二题", 71.55],["第三题", 63.60],["第四题", 62.72],["第五题", 62.44],["第六题", 62.18],["第七题", 61.54]

    plot_bar_with_percent(data_1)
