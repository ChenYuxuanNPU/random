import copy

from func import *

edu_bg_list = sorted(
    del_tuple_in_list(data=execute_sql_sentence(sentence=f'select distinct "最高学历" from teacher_data_0_2024')),
    key=lambda x: get_educational_background_order()[x]) + ["高一级学历"] + ['合计']

edu_base_dict = {item: 0 for item in edu_bg_list}

period_list = sorted(
    del_tuple_in_list(data=execute_sql_sentence(sentence=f'select distinct "任教学段" from teacher_data_0_2024')),
    key=lambda x: get_period_order()[x]
)

period_base_dict = {item: copy.deepcopy(edu_base_dict) for item in period_list}

school_list = execute_sql_sentence(
    sentence=f'select "校名",count(*) from teacher_data_0_2024 group by "校名" order by count(*) desc')

output = {school[0]: copy.deepcopy(period_base_dict) for school in school_list}

crude_data = execute_sql_sentence(sentence=f'select "校名", "任教学段","最高学历" from teacher_data_0_2024')

supplement_info_dict = {}
for item in crude_data:

    if item[0] not in supplement_info_dict.keys():
        supplement_info_dict[item[0]] = {"义务教育高一级学历": 0, "义务教育总数": 0}

    output[item[0]][item[1]][item[2]] += 1
    output[item[0]][item[1]]["合计"] += 1

    if item[1] in ["小学", "初中"]:
        supplement_info_dict[item[0]]["义务教育总数"] += 1

    if item[1] == "小学" and item[2] in ["博士研究生", "硕士研究生", "本科", "专科"]:
        output[item[0]][item[1]]["高一级学历"] += 1
        supplement_info_dict[item[0]]["义务教育高一级学历"] += 1

    if item[1] == "初中" and item[2] in ["博士研究生", "硕士研究生", "本科", ]:
        output[item[0]][item[1]]["高一级学历"] += 1
        supplement_info_dict[item[0]]["义务教育高一级学历"] += 1

print(supplement_info_dict)

output_list = []
row0 = [""]
row1 = [""]
for school, data0 in output.items():
    for period, data1 in data0.items():
        for edu_bg, data2 in data1.items():
            # print([school, period, edu_bg, data2])
            row0.append(period)
            row1.append(edu_bg)
    break

row0.extend(["义务教育阶段", "义务教育阶段"])
row1.extend(["高于规定学历", "总数"])

output_list.append(row0)
output_list.append(row1)

for school, data0 in output.items():
    temp = [school]
    for period, data1 in data0.items():
        for edu_bg, data2 in data1.items():
            temp.append(data2)
    temp.extend([supplement_info_dict[school]["义务教育高一级学历"], supplement_info_dict[school]["义务教育总数"]])

    output_list.append(temp)

save_excel(two_dimension_list=output_list, excel_name="output")
