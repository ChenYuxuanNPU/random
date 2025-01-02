import copy

from func import *

edu_bg_list = sorted(
    del_tuple_in_list(data=execute_sql_sentence(sentence=f'select distinct "最高学历" from teacher_data_1_2024')),
    key=lambda x: get_educational_background_order()[x]) + ["高一级学历"] + ['合计']

print(edu_bg_list)

edu_base_dict = {item: 0 for item in edu_bg_list}

period_list = sorted(
    del_tuple_in_list(data=execute_sql_sentence(sentence=f'select distinct "任教学段" from teacher_data_0_2024')),
    key=lambda x: get_period_order()[x]
)

period_base_dict = {item: copy.deepcopy(edu_base_dict) for item in period_list}

school_list = execute_sql_sentence(
    sentence=f'select "校名",count(*) from teacher_data_0_2024 where "学校类型" not in ("幼儿园","教学支撑单位") group by "校名" order by count(*) desc')
school_list.extend(execute_sql_sentence(
    sentence=f'select "校名",count(*) from teacher_data_1_2024 where "学校类型" not in ("幼儿园","教学支撑单位") group by "校名" order by count(*) desc'))
# print(school_list)

output = {school[0]: {kind: copy.deepcopy(period_base_dict) for kind in ["在编", "编外"]} for school in school_list}
# print(output)

crude_data = execute_sql_sentence(sentence=f'select "校名", "任教学段","最高学历", "在编" from teacher_data_0_2024 where "学校类型" not in ("幼儿园","教学支撑单位")')
crude_data.extend(execute_sql_sentence(
    sentence=f'select "校名", "任教学段","最高学历", "编外" from teacher_data_1_2024 where "任教学段" in ("高中","初中","小学","幼儿园","中职") and "主教学科" not in ("无","其他") and "学校类型" not in ("幼儿园","教学支撑单位")'))
# print(crude_data)

supplement_info_dict = {school[0]: {"义务教育高一级学历": 0, "义务教育总数": 0} for school in school_list}
for item in crude_data:

    output[item[0]][item[3]][item[1]][item[2]] += 1
    output[item[0]][item[3]][item[1]]["合计"] += 1

    if item[1] in ["小学", "初中"]:
        supplement_info_dict[item[0]]["义务教育总数"] += 1

    if item[1] == "小学" and item[2] in ["博士研究生", "硕士研究生", "本科", "专科"]:
        output[item[0]][item[3]][item[1]]["高一级学历"] += 1
        supplement_info_dict[item[0]]["义务教育高一级学历"] += 1

    if item[1] == "初中" and item[2] in ["博士研究生", "硕士研究生", "本科", ]:
        output[item[0]][item[3]][item[1]]["高一级学历"] += 1
        supplement_info_dict[item[0]]["义务教育高一级学历"] += 1

# print(supplement_info_dict)

output_list = []
row0 = [""]
row1 = [""]
row2 = [""]

for school, data0 in output.items():
    for kind, data1 in data0.items():
        for period, data2 in data1.items():
            for edu_bg, data3 in data2.items():
                # print([school, period, edu_bg, data3])
                row0.append(kind)
                row1.append(period)
                row2.append(edu_bg)
    break

row0.extend(["合计", "合计", "合计"])
row1.extend(["义务教育阶段", "义务教育阶段", "义务教育阶段"])
row2.extend(["高于规定学历", "总数", "占比"])

output_list.append(row0)
output_list.append(row1)
output_list.append(row2)

for school, data0 in output.items():
    temp = [school]
    for kind, data1 in data0.items():
        for period, data2 in data1.items():
            for edu_bg, data3 in data2.items():
                temp.append(data3)
    temp.extend([supplement_info_dict[school]["义务教育高一级学历"], supplement_info_dict[school]["义务教育总数"], 1 if supplement_info_dict[school]["义务教育总数"] == 0 else round(supplement_info_dict[school]["义务教育高一级学历"]/supplement_info_dict[school]["义务教育总数"],2)])

    output_list.append(temp)

save_excel(two_dimension_list=output_list, excel_name="output")
