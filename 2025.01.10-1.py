from func import *

order_dict = {
    "高级中学": 100,
    "高等学校": 100,
    "初级中学": 90,
    "初中": 90,
    "中职专业课": 90,
    "中职": 90,
    "小学": 80,
    "幼儿园": 50
}

count_dict = {
    "初中": {},
    "小学": {}
}

result0 = execute_sql_sentence(
    sentence=f'select "校名", "任教学段","教师资格学段" , count(*) from teacher_data_0_2024 where "教师资格学段" != "无" and "任教学段" in ("初中","小学") group by "校名","任教学段", "教师资格学段"')
# print(len(set([item[0] for item in result0])))

result0_sum = execute_sql_sentence(
    sentence=f'select "校名","任教学段",count(*) from teacher_data_0_2024 where "任教学段" in ("初中","小学") group by "校名","任教学段"')
# print(len(set([item[0] for item in result0_sum])))

for item in result0_sum:
    if item[0] not in count_dict["初中"].keys() and item[1] == "初中":
        count_dict["初中"][item[0]] = item[2]

    elif item[0] not in count_dict["小学"].keys() and item[1] == "小学":
        count_dict["小学"][item[0]] = item[2]

    elif item[1] == "初中" and item[0] in count_dict["初中"].keys():
        count_dict["初中"][item[0]] += item[2]

    elif item[1] == "小学" and item[0] in count_dict["小学"].keys():
        count_dict["小学"][item[0]] += item[2]
    else:
        print(111)

result1 = execute_sql_sentence(
    sentence=f'select "校名", "任教学段","教师资格学段" , count(*) from teacher_data_1_2024 where "教师资格学段" != "无" and "任教学段" in ("初中","小学") group by "校名","任教学段", "教师资格学段"'
)
# print(len(set([item[0] for item in result1])))

result1_sum = execute_sql_sentence(
    sentence=f'select "校名","任教学段",count(*) from teacher_data_1_2024 where "任教学段" in ("初中","小学") group by "校名","任教学段"')
# print(len(set([item[0] for item in result1_sum])))

for item in result1_sum:
    if item[0] not in count_dict["初中"].keys() and item[1] == "初中":
        count_dict["初中"][item[0]] = item[2]

    elif item[0] not in count_dict["小学"].keys() and item[1] == "小学":
        count_dict["小学"][item[0]] = item[2]

    elif item[1] == "初中" and item[0] in count_dict["初中"].keys():
        count_dict["初中"][item[0]] += item[2]

    elif item[1] == "小学" and item[0] in count_dict["小学"].keys():
        count_dict["小学"][item[0]] += item[2]
    else:
        print(111)
        print(item)

output_p = {}
output_j = {}
# {"校名":["总人数","合理教资数","不合理教资数"]}

for item in result0 + result1:
    if item[1] == "初中":
        if item[0] not in output_j:
            output_j[item[0]] = [0, 0, 0]

    elif item[1] == "小学":
        if item[0] not in output_p:
            output_p[item[0]] = [0, 0, 0]

    else:
        print(111)

for item in result0 + result1:

    if item[1] == "初中":
        if order_dict[item[1]] > order_dict[item[2]]:
            output_j[item[0]][2] += item[3]
        else:
            output_j[item[0]][1] += item[3]

    elif item[1] == "小学":
        if order_dict[item[1]] > order_dict[item[2]]:
            output_p[item[0]][2] += item[3]
        else:
            output_p[item[0]][1] += item[3]

for key, value in output_j.items():
    output_j[key][0] = count_dict["初中"][key]

for key, value in output_p.items():
    output_p[key][0] = count_dict["小学"][key]

# list_p = [["校名", "总人数", "持教资且学段符合人数", "持不符合学段教资人数"]]
list_p = []
for key, value in output_p.items():
    temp = [key]
    temp.extend(value)
    list_p.append(temp)

save_excel(two_dimension_list=list_p, excel_name="小学")

# list_j = [["校名", "总人数", "持教资且学段符合人数", "持不符合学段教资人数"]]
list_j = []
for key, value in output_j.items():
    temp = [key]
    temp.extend(value)
    list_j.append(temp)

save_excel(two_dimension_list=list_j, excel_name="初中")



