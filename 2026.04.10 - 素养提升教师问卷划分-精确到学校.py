"""
这个文件做人数统计、表格划分
"""

from func import *
from collections import Counter

data = read_xlsx_to_list(file_path=fr"2026.04.10 - 优均问卷/1.xlsx")

title = data[0]

ans = data[1:]

schools = ["广州市白云区白云实验学校（初中部）","广州市白云区广大附中实验中学（北校区）","广州市白云区广附云湖实验学校（初中部）","广州市白云区石井中学","广州市白云区龙归学校总校区初中部","广州市白云区黄石学校（黄石校区初中部）","广州市白云区嘉禾中学","广州市白云区江高镇第二初级中学","广州市白云区广东第二师范学院实验中学（初中部）","广州市白云区竹料第一中学（南校区）"]


output = {}
for item in schools:
    output[item] = []

for item in ans:
    output[item[1]].append(item)

for key in output.keys():
    temp = [title]

    for item in output[key]:
        temp.append(item)

    save_excel(two_dimension_list=temp,excel_name=fr"2026.04.10 - 优均问卷/问卷划分/分学校/{key}问卷原始结果")

