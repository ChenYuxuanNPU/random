import copy
from collections import Counter

from func import *

data = read_xlsx_to_list(file_path=fr"0319/1.xlsx")

counter_list = Counter([item[4] for item in data])

redundant_id_list = [key for key in counter_list if counter_list[key] > 1]

# # 用来排除金广实验和广大附中实验中学的重复考核结果
# output = []
# count = 0
# for item in data:
#     if item[4] not in redundant_id_list or item[2] not in ["广州市白云区金广实验学校","广州市白云区广大附中实验中学"]:
#         output.append(item)
#
#     elif item[4] in redundant_id_list and item[2] == "广州市白云区金广实验学校":
#         for i in data:
#             if item[4] == i[4] and i[2] == "广州市白云区广大附中实验中学":
#                 output.append(i)
#                 count += 1
# save_excel(two_dimension_list=output,excel_name="output")

# 用来删除所有完全相同的行
output = []
count = 0
data_tuple = [tuple(item) for item in data]

print(max(v for v in Counter(data_tuple).values()))

dict_1 = copy.deepcopy(dict(Counter(data_tuple)))

for item in data:
    if dict_1[tuple(item)] > 1:
        count += 1
        output.append(item)
        dict_1[tuple(item)] = 0
    elif dict_1[tuple(item)] == 1:
        output.append(item)

save_excel(output, "output")
