import copy

from func import *

data = read_xlsx_to_list(file_path=fr"2026.11.02.xlsx")

check_dict = {}

result = []

for item in data:
    item = tuple(item)
    if item not in check_dict.keys():
        check_dict[item] = 1
    else:
        check_dict[item] += 1

for key,value in check_dict.items():
    temp = list(copy.deepcopy(key))
    temp.append(value)
    result.append(temp)

result.sort(key=lambda x: (x[0], x[1], x[2], x[3]))

print(result)

save_excel(two_dimension_list=result,excel_name="学生信息表格")