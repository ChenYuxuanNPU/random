"""
教师问卷结果统计
"""

from func import *

raw_data = read_xlsx_to_list(file_path="1.xlsx")

# print(raw_data)

output_dict = {}

question_list = raw_data[0]  # 第一项是校名

answer_list = raw_data[1:]

# print(answer_list)

for ans in answer_list:

    school_name = ans[0]
    if school_name not in output_dict.keys():
        output_dict[school_name] = {question: {"总数": 0} for question in question_list[1:]}

    for i in range(1, len(ans)):
        if ans[i] in output_dict[school_name][question_list[i]].keys():
            output_dict[school_name][question_list[i]][ans[i]] += 1
        else:
            output_dict[school_name][question_list[i]][ans[i]] = 1

        output_dict[school_name][question_list[i]]["总数"] += 1

print(output_dict)
