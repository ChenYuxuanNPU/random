from func import *

data = read_xlsx_to_list(file_path=fr"2026.03.16/1.xlsx")

real_data = read_xlsx_to_list(file_path=fr"2026.03.16/人次.xlsx")

id_list = [item[3] for item in real_data]

check = {}

for item in data:
    if item[4] in id_list or str(item[4]) in id_list:
        if item[4] not in check:
            check[item[4]] = {
                "姓名": item[3],
                "学校": item[2],
                "考核结果": item[9],
            }

        else:
            if item[3] == check[item[4]]["姓名"] and item[9] == check[item[4]]["考核结果"]:
                pass

            if item[9] != check[item[4]]["考核结果"]:
                print(fr"{item[4]}考核结果不符合")

            if item[3] != check[item[4]]["姓名"]:
                print(fr"{item[4]}姓名不符合")

for id in id_list:

    if id not in check.keys():
        for item in real_data:
            if id == item[3] and "教育综合服务中心" not in item[1]:
                print(item)
