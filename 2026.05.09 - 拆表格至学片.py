from func import *

subject = "英语"
title = read_xlsx_to_list(fr"0509/{subject}.xlsx")[0]
data = read_xlsx_to_list(fr"0509/{subject}.xlsx")[1:]

output = {

}

for item in data:
    if item[0] in output.keys():
        output[item[0]].append(item)
    else:
        output[item[0]] = []
        output[item[0]].append(item)

for key in output.keys():
    temp = [title]
    for item in output[key]:
        temp.append(item)
    save_excel(two_dimension_list=temp,excel_name=fr"0509/{subject} - {key}")