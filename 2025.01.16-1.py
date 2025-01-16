from func import *
import pandas as pd

period_list = ["高中", "初中", "小学", "幼儿园"]
area_list = ["永平", "石井", "江高", "人和", "新市", "太和", "钟落潭"]

result_a0 = execute_sql_sentence(
    sentence=f'select "校名", "任教学段","区域", count(*) from teacher_data_0_2024 where "任教学段" not in ("无", "其他","高中") and "区域" != "直管" group by "区域","校名", "任教学段"'
)
# print(result_a0)

result_a1 = execute_sql_sentence(
    sentence=f'select "校名", "任教学段","区域", count(*) from teacher_data_1_2024 where "任教学段" not in ("无", "其他","高中") and "区域" != "直管" group by "区域","校名", "任教学段"'
)
# print(result_a1)

output_0 = {area: {period: 0 for period in period_list if period != "高中"} for area in area_list}

for item in result_a0 + result_a1:
    output_0[item[2]][item[1]] += item[3]

print(output_0)
df = pd.DataFrame.from_dict(output_0, orient='index')
df.to_excel('初中及以下.xlsx', index=True)

output_1 = {}
result_z0 = execute_sql_sentence(
    sentence=f'select "校名", "任教学段","区域", count(*) from teacher_data_0_2024 where "任教学段" not in ("无", "其他","高中") and "区域" = "直管" group by "校名", "任教学段","区域"'
)
# print(result_z0)

result_z1 = execute_sql_sentence(
    sentence=f'select "校名", "任教学段","区域", count(*) from teacher_data_1_2024 where "任教学段" not in ("无", "其他","高中") and "区域" = "直管" group by "校名", "任教学段","区域"'
)
# print(result_z1)

for item in result_z0 + result_z1:

    if item[0] not in output_1.keys():
        output_1[item[0]] = {period: 0 for period in period_list + ["中职"]}
        output_1[item[0]][item[1]] += item[3]
    else:
        output_1[item[0]][item[1]] += item[3]

print(output_1)

df = pd.DataFrame.from_dict(output_1, orient='index')
df.to_excel('直管初中及以下.xlsx', index=True)


result_g0 = execute_sql_sentence(
    sentence=f'select "校名", count(*) from teacher_data_0_2024 where "任教学段" = "高中" group by "校名"'
)

# print(result_g0)

result_g1 = execute_sql_sentence(
    sentence=f'select "校名", count(*) from teacher_data_1_2024 where "任教学段" = "高中" group by "校名"'
)

# print(result_g1)

output_2 = {}
for item in result_g0 + result_g1:

    if item[0] not in output_2.keys():
        output_2[item[0]] = int(item[1])
    else:
        output_2[item[0]] += int(item[1])

print(output_2)
df = pd.DataFrame.from_dict(output_2, orient='index')
df.to_excel('直管高中.xlsx', index=True)