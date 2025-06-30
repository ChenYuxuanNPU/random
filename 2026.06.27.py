"""
用于统计中小学教师学历层次和年龄结构情况表
"""

from func import *

data = execute_sql_sentence(
    sentence='select "身份证号","参加工作前毕业院校代码","参加工作前学历","行政职务","入编时间","姓名" from teacher_data_0 where "采集年份" == "2024"'
)

data.extend(
    read_xlsx_to_list(file_path=fr"C:\Users\1012986131\Desktop\2025data.xlsx", sheet_name="Sheet1")
)

for i in range(len(data)):
    data[i] = list(data[i])
    data[i][0] = get_age_from_citizen_id(citizen_id=data[i][0], )

#  ["无", "副校级", "党组织书记兼校长", "正校级", "党组织书记"]
# data_list_0 = [item for item in data if
#                51 <= item[0] <= 500
#                and item[2] == "本科"
#                and item[1] not in get_code_of_211()
#                and item[-1][0:4] in ["2025", "2024", "2023"]
#                ]
#
# print(len(data_list_0))

for item in data:
    if item[4][0:4] in ["2025","2024","2023"] and item[0] >= 51:
        print(item)
