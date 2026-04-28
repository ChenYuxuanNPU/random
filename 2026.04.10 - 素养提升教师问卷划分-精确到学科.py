"""
这个文件做人数统计、表格划分
"""

from func import *
from collections import Counter


def custom_sort_2d(data):
    """
    data: 二维列表，如 [['B', 'Y'], ['A', 'X'], ['B', 'X']]
    order_first: 第一项的自定义顺序列表，如 ['A', 'B', 'C']
    order_second: 第二项的自定义顺序列表，如 ['X', 'Y', 'Z']
    """
    # 建立映射：值 -> 排序序号（未出现的值放到最后）
    order_first = ["广州市白云区白云实验学校（初中部）", "广州市白云区广大附中实验中学（北校区）",
                   "广州市白云区广附云湖实验学校（初中部）", "广州市白云区石井中学", "广州市白云区龙归学校总校区初中部",
                   "广州市白云区黄石学校（黄石校区初中部）", "广州市白云区嘉禾中学", "广州市白云区江高镇第二初级中学",
                   "广州市白云区广东第二师范学院实验中学（初中部）", "广州市白云区竹料第一中学（南校区）"]

    order_second = ["语文", "数学", "英语", "物理", "地理", "生物", "音乐", "美术", "体育", "道法", "劳动"]

    rank_first = {val: idx for idx, val in enumerate(order_first)}
    rank_second = {val: idx for idx, val in enumerate(order_second)}

    def sort_key(item):
        # 如果值不在映射中，给一个很大的序号（相当于排在最后）
        k1 = rank_first.get(item[0], len(order_first))
        k2 = rank_second.get(item[1], len(order_second))
        return (k1, k2)

    return sorted(data, key=sort_key)


data = read_xlsx_to_list(file_path=fr"2026.04.10 - 优均问卷/1.xlsx")

title = data[0]

ans = data[1:]

count_list = Counter(custom_sort_2d(list([(item[1], item[6]) for item in ans])))

keys = custom_sort_2d(set([(item[1], item[6]) for item in ans]))

output = {}
for item in keys:
    output[item] = []

for item in ans:
    output[(item[1], item[6])].append(item)

for key in output.keys():
    temp = [title]

    for item in output[key]:
        temp.append(item)

    save_excel(two_dimension_list=temp,
               excel_name=fr"2026.04.10 - 优均问卷/问卷划分/分学科/{key[0]}：{key[1]}问卷原始结果")
