import pandas as pd
import json

# 读取 Excel 文件
file_path = '院校代码.xlsx'
df = pd.read_excel(file_path, header=None)  # 如果文件没有标题行，使用 header=None

# 将 DataFrame 转换为二维列表
data_list = df.values.tolist()

# 打印二维列表
# for row in data_list:
#     print(row)

dict = {}

for row in data_list:
    dict[row[0]] = [str(item) for item in row[1:]]

print(dict)

with open("院校代码.json", 'w', encoding='utf-8') as json_file:
    json.dump(dict, json_file, ensure_ascii=False, indent=4)