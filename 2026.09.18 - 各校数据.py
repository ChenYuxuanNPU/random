from collections import Counter
from collections import defaultdict

import matplotlib.pyplot as plt

from func import *


def school_avg_scores(students):
    """
    参数:
        students: 二维列表, 每个子列表为 [学校id(str), 成绩]
                  例如 [['A', 90], ['B', 85], ['A', 70]]

    返回:
        二维列表, 每个子列表为 [学校id, 均分], 按均分从高到低排列
    """
    # 1. 累加各学校总分和人数
    total = defaultdict(float)
    count = defaultdict(int)

    for school_id, score in students:
        total[school_id] += score
        count[school_id] += 1

    # 2. 计算均分
    result = [[sid, round(total[sid] / count[sid], 2)] for sid in total]

    # 3. 按均分从高到低排序
    result.sort(key=lambda x: x[1], reverse=True)

    return result


def plot_frequency(data, value_range=(0, 100), title='学校信息', step=1):
    """
    统计一元整数列表中每个值的出现次数, 并绘制柱状图

    参数:
        data: 整数列表, 如 [55, 56, 70, 55]
        value_range: 横轴显示范围, 默认 (0, 100)
        title: 图表标题
        step: 精度, 默认 1
    """
    if not data:
        print("数据为空")
        return

    # 1. 统计每个值出现的次数
    counts = Counter(data)
    values = sorted(counts.keys())
    freqs = [counts[v] for v in values]

    # 2. 横轴范围 (对齐到 step)
    lo = min(min(data), value_range[0])
    hi = max(max(data), value_range[1])
    lo = (lo // step) * step
    hi = ((hi // step) + 1) * step

    # 3. 中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots(figsize=(12, 5))

    # 4. 画柱子
    ax.bar(values, freqs, width=step, color='steelblue', edgecolor='white')

    for v, f in zip(values, freqs):
        ax.text(v, f, str(f), ha='center', va='bottom', fontsize=10)

    # 5. 坐标轴
    ax.set_xlim(lo, hi)
    ax.set_ylim(0, max(freqs) + 1)
    ax.set_xticks(range(int(lo), int(hi) + 1, 1))
    ax.set_xlabel('学校数据')
    ax.set_ylabel('学校数量')
    ax.set_title(title, fontsize=14)
    ax.grid(axis='y', linestyle='--', alpha=0.4)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    data = [[item[0], item[4]] for item in read_xlsx_to_list(file_path=fr"0917.xlsx")]

    print(school_avg_scores(data))

    data_1 = [int(item[1]) for item in school_avg_scores(data)]

    plot_frequency(data_1, value_range=(6, 13), title="打字题")
