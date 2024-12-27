"""
统计科学教师情况
"""

from func import *

result = []
for year in [2023, 2024]:
    result.extend(execute_sql_sentence(
        sentence=f'select "姓名", "校名", "任教学段", "{year}" from teacher_data_0_{year} where "主教学科" = "科学"'
    ))

print(result)

# 读取 Excel 文件
workbook = openpyxl.Workbook()

# 获取活动的工作表
ws = workbook.active

for item in result:
    ws.append(item)

# 保存工作簿到文件
workbook.save("output.xlsx")
