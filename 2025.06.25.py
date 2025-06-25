"""
判断学号是不是都没问题
1.判断中间三位是否都在学校代码列表里
2.判断所有学生学号是否都在学生名册里
"""

from func import *

school_id_check = {item[0]: item[1] for item in read_xlsx_to_list(
    file_path=r"C:\Users\1012986131\Desktop\2024学年下学期期末诊断调研质量分析\初中学校.xlsx",
    sheet_name="Sheet1"
)[1:]}

grade = "八年级"

data = read_xlsx_to_list(
    file_path=r"C:\Users\1012986131\Desktop\2024学年下学期期末诊断调研质量分析\信息科技考试数据源.xlsx",
    sheet_name=grade)[1:]

#  用于判断那三位是否在学校列表里
# stu_id_list = [str(item[0])[2:5] for item in data]
#
# for item in stu_id_list:
#     if item not in school_id_check:
#         print("fuck!")

#  用于判断学生id是否长度相等
# stu_id_list = [str(item[0]) for item in data]
#
# id_len = len(stu_id_list[0])
#
# for item in stu_id_list:
#     if len(item) != id_len:
#         print("fuck!")

#  学生名册的正确学生id
stu_id_check = read_xlsx_to_list(
    file_path=fr"C:\Users\1012986131\Desktop\2024学年下学期期末诊断调研质量分析\{grade}学生名册.xlsx",
    sheet_name="Sheet1")[1:]

stu_id_check = [item[0] for item in stu_id_check]

# 考生数据中的id
stu_id_list = [str(item[0]) for item in data]

for item in stu_id_list:
    if item not in stu_id_check:
        print(item)

