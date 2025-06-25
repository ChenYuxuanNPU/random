"""
用于发布不同学校的等级情况
"""
from func import *
import os

grade = "七年级"

data = read_xlsx_to_list(
    file_path=r"C:\Users\1012986131\Desktop\2024学年下学期期末诊断调研质量分析\信息科技考试数据源.xlsx",
    sheet_name=grade)

print(data[1])

output = {area: {} for area in ["新市", "永平", "石井", "江高", "人和", "太和", "钟落潭"]}

for area in ["新市", "永平", "石井", "江高", "人和", "太和", "钟落潭"]:
    os.mkdir(area)

sheet_title = ["考号", "姓名", "年级", "班级", "等级"]

for item in data[1:]:

    if item[-2] not in output[item[-1]].keys():
        output[item[-1]][item[-2]] = []

    output[item[-1]][item[-2]].extend([item[0:4] + [item[13]]])

print(output)

for area, schools in output.items():
    for school, data_list in schools.items():
        save_excel(
            two_dimension_list=[sheet_title] + output[area][school],
            excel_name=fr"{area}/{school}"
        )
