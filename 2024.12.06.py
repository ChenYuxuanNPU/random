import pandas as pd
import openpyxl

from func import *


# 读取 Excel 文件
file_path = 'base.xlsx'
df = pd.read_excel(file_path, header=None)  # 如果文件没有标题行，使用 header=None

# 将 DataFrame 转换为二维列表
data_list = del_tuple_in_list(df.values.tolist())

print(data_list)

workbook = openpyxl.Workbook()

# 获取活动的工作表
ws = workbook.active

for name in data_list:
    output = []
    result = execute_sql_sentence(sentence=f'select "校名", "身份证号", "手机号" from teacher_data_0_2024 where "姓名" = "{name}"')
    print(result)
    if len(result) > 1:
        print("?")

    if not result:
        output.append(name)
    else:
        output.append(name)
        output.extend(result[0])
    print(output)
    ws.append(output)

# 保存工作簿到文件
workbook.save("output.xlsx")
