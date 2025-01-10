from func import *

raw_result = read_xlsx_to_list(file_path=fr"C:\Users\1012986131\Desktop\python\random\input.xlsx")

print(raw_result)

check_dict = {}

for item in raw_result:
    if item[1] not in check_dict.keys():
        check_dict[item[1]] = [item[0], float(item[2]), item[3]]
    else:
        check_dict[item[1]][1] += item[2]


print(len(check_dict.keys()))

output = []
for key, value in check_dict.items():
    output.append([value[0], key, value[1], value[2]])

save_excel(two_dimension_list=output, excel_name="output")
