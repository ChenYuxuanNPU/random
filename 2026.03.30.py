from collections import Counter

from func import *

data = read_xlsx_to_list(fr"temp-0330.xlsx")

data_0 = [item for item in data[0] if item[1] == "年度考核"]
data_1 = [item for item in data[0] if item[1] == "师德考核"]
data_2 = [item for item in data[0] if item[1] == "嘉奖"]

check_list = [item[0] for item in data]

check_dict = Counter(check_list)

output = []

for key, value in check_dict.items():

    check = [item[1] for item in data if item[0] == key]
    if "年度考核" not in check or "师德考核" not in check:
        temp = [item for item in data if item[0] == key]
        if temp[0][-1] != "广州市白云区教育综合服务中心":
            output.extend(temp)
            output.append([""])

print(output)

save_excel(output, "output")
