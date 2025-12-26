from func import *

data = read_xlsx_to_list(file_path=fr"C:\Users\1012986131\Desktop\新建 XLSX 工作表.xlsx", sheet_name="Sheet2")[1:]
print(data)

school_0_list = []

for item in data:
    if item[0] == "公办" and item[2] not in school_0_list:
        school_0_list.append(item[2])

school_0_list = list(set(school_0_list))

output_0 = [0, 0, 0, 0, 0]
output_1 = [0, 0, 0, 0, 0]
# 幼儿园 小学 初中 高中 中职
dict1 = {
    "幼儿园": 0,
    "小学": 1,
    "初中": 2,
    "高中": 3,
    "中职": 4
}

for item in data:
    if item[2] in school_0_list:
        if int(item[1]) < 40 and 1900 < int(item[3]) <= 2022:
            output_0[dict1[item[-1]]] += 1
    else:
        if int(item[1]) < 40 and 1900 < int(item[3]) <= 2022:
            output_1[dict1[item[-1]]] += 1

print(output_0)
print(output_1)

