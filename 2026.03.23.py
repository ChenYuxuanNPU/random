"""
用来处理学生问卷统计的结果
"""

from func import *

data = read_xlsx_to_list(file_path=fr"2026.03.23 - 学生问卷/学生问卷.xlsx")

for i in range(len(data)):
    for k in range(2, len(data[i])):
        if data[i][k] not in ["A", "B", "C", "D", ]:
            data[i][k] = "S"

output = [["题号"]]
for i in ["A", "B", "C", "D", ]:
    output[0].append(f"选{i}人数")
    output[0].append(f"选{i}占比")
output[0].append("未选人数")
output[0].append("未选占比")

for i in range(len(data[0]) - 2):
    output.append([f"第{i + 1}题"] + [0] * 10)

ans_location = {
    "A": 1,
    "B": 3,
    "C": 5,
    "D": 7,
    "S": 9
}

for item in data[1:]:
    ans = item[2:]

    for k in range(len(ans)):
        output[k + 1][ans_location[ans[k]]] += 1

for i in range(1, len(output)):
    for k in range(2, len(output[i]), 2):
        output[i][k] = f"{round(output[i][k - 1] / len(data[1:]) * 100, 2)}%"

save_excel(output, "2026.03.23 - 学生问卷/学生问卷统计结果")
