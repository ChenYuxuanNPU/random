import copy

from func import *
from collections import Counter
import os

path = "2026.04.10 - 优均问卷/问卷划分/分学科"
file_name_list = copy.deepcopy(os.listdir(path))

for file in file_name_list:

    data = read_xlsx_to_list(file_path=fr"{path}/{file}")
    title = data[0]
    ans = data[1:]

    output = []
    temp = []

    for i in range(3,27):
        if i != 7:
            temp=[[title[i],"人数","占比"]]

            ans_i = [item[i] for item in ans]
            statistic = dict(Counter(sorted(ans_i)))
            for key in statistic.keys():
                temp.append([key,statistic[key],fr"{round(statistic[key] / sum([value for value in statistic.values()]) * 100,2)}%"])

            temp.append([])

            output.extend(temp)

    save_excel(output,fr"{path}/{file} - 统计结果")


