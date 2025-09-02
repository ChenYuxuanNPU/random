from func import *

data_0 = execute_sql_sentence(
    sentence=f'select "校名","任教学段","区域" from teacher_data_0 where "采集年份" == 2024 and ("任教学段" == "小学" or "任教学段" == "初中") and "学校类型" != "教学支撑单位"'
)

data_1 = execute_sql_sentence(
    sentence=f'select "校名","任教学段","区域" from teacher_data_1 where "采集年份" == 2024 and ("任教学段" == "小学" or "任教学段" == "初中") and "学校类型" != "教学支撑单位"'
)

school_list_0 = list(set([item[0] for item in data_0]))
school_list_1 = list(set([item[0] for item in data_1 if item[0] not in school_list_0]))

output = {key: {"初中": {"合计": 0, "公办": 0, "民办": 0}, "小学": {"合计": 0, "公办": 0, "民办": 0}} for key in
          ["新市", "永平", "石井", "江高", "人和", "太和", "钟落潭", "直管"]}

for item in data_0 + data_1:
    output[item[2]][item[1]]["合计"] += 1

    if item[0] in school_list_0:
        output[item[2]][item[1]]["公办"] += 1
    else:
        output[item[2]][item[1]]["民办"] += 1

data = data_0 + data_1

output_1 = {}
for item in data:
    if item[2] == "直管":
        if item[0] not in output_1.keys():
            output_1[item[0]] = {"初中": 0, "小学": 0}
        output_1[item[0]][item[1]] += 1

print(output_1)
