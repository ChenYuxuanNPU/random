import pandas as pd
import openpyxl

from func import *


# 读取 Excel 文件
file_path = 'base.xlsx'
df = pd.read_excel(file_path, header=None)  # 如果文件没有标题行，使用 header=None

# 将 DataFrame 转换为二维列表
data_list = df.values.tolist()

print(data_list)

for i in range(len(data_list)):
    result = execute_sql_sentence(sentence=f'select "身份证号", "手机号" from teacher_data_0_2024 where "姓名" = "{data_list[i][0]}" and "校名" = "{data_list[i][1]}"')
    print(result)
    for item in result:
        for item1 in item:
            data_list[i].append(item1)
    if len(result) != 1:
        print(data_list[i])

print(data_list)

workbook = openpyxl.Workbook()

# 获取活动的工作表
ws = workbook.active

for data in data_list:
    ws.append(data)

# 保存工作簿到文件
workbook.save("output.xlsx")

