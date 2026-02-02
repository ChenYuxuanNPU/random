from func import *

list_1 = ['新市片', '永平片', '石井片', '江高镇', '人和镇', '太和镇', '钟落潭镇']

file_name = fr"0202/初一B-等级汇总表.xlsx"
excel_name = file_name.split("/")[1].split(".")[0]
print(excel_name)

data = read_xlsx_to_list(file_name)

output = {item: [data[0]] for item in list_1}

for item in data[1:]:
    output[item[4]].append(item)

print(output)

for key, value in output.items():
    save_excel(two_dimension_list=value, excel_name=fr"0202/{key}/{excel_name}")
