"""
统计科学教师情况
"""

from func import *

# 读取 Excel 文件
workbook = openpyxl.Workbook()

# 获取活动的工作表
ws = workbook.active

result = []
for year in [2023, 2024]:
    result.extend(execute_sql_sentence(
        sentence=f'select "姓名", "身份证号"from teacher_data_0_{year} where "主教学科" = "科学"'
    ))
print(len(result))
result = set(result)
print(len(result))
temp = []
excel_output = []
for name, id in result:
    temp = execute_sql_sentence(
        sentence=f'select "姓名", "校名", "任教学段", "主教学科", "2023" from teacher_data_0_2023 where "姓名" = "{name}" and "身份证号" = "{id}" union all select "姓名", "校名", "任教学段", "主教学科", "2024" from teacher_data_0_2024 where "姓名" = "{name}" and "身份证号" = "{id}" '
    )

    if len(temp) == 2:
        excel_output.append(temp[0])
        excel_output.extend(temp[1:])

    else:
        excel_output.append(temp[0])

print(excel_output)
print(len(set(excel_output)))

for i in range(len(excel_output)):
    if i != len(excel_output) - 1 and excel_output[i][0] == excel_output[i + 1][0]:
        ws.append(excel_output[i] + excel_output[i + 1])

    elif i >= 1 and excel_output[i][0] == excel_output[i - 1][0]:
        continue

    else:
        if excel_output[i][4] == "2023":
            ws.append(excel_output[i])
        else:
            ws.append(["","","","",""] + list(excel_output[i]))

# 保存工作簿到文件
# workbook.save("output.xlsx")

names = ["某些姓名"]

for name in names:
    if name not in [a[0] for a in result]:
        print(name)
