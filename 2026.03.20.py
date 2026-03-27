from collections import Counter

from func import *

data = read_xlsx_to_list(file_path=fr"0319/1.xlsx")

counter_list = Counter([item[3] for item in data])

redundant_id_list = [key for key in counter_list if counter_list[key] > 1]
print(len(redundant_id_list))

output = []

for re_id in redundant_id_list:
    for item in data:
        if item[3] == re_id:
            output.append(item)
save_excel(output, "output")
print(output)
