"""
用于统计我区2025年定期奖励结果
备注：
2026.03.16是师德考核，要求定期奖励结果中所有教师师德考核合格及以上
培英中学少了一个嘉奖指标给了民航学校的张兵
石井片嘉奖是228个，只报了227个，原因是分配到沙凤小学的1个老师自已放弃不报，学校也不补
"""
from typing import Counter

from func import *

# 检查所有直管单位和片镇定期奖励是否超过指标数
limit_dict = {}

for key, value in read_xlsx_to_list(file_path=fr"2026.03.17/指标分配.xlsx"):
    limit_dict[key] = value

data = read_xlsx_to_list(file_path=fr"2026.03.17/1.xlsx")

high_school_data = [item[5] for item in data if item[1] == "直管"]
high_school_counter = Counter(high_school_data)

area_data = [item[1] for item in data if item[1] != "直管"]
area_counter = Counter(area_data)

for key in high_school_counter.keys():
    if high_school_counter[key] > limit_dict[key]:
        print(fr"{key}指标不满足：现有{high_school_counter[key]}，上限为{limit_dict[key]}")
    elif high_school_counter[key] < limit_dict[key]:
        print(fr"{key}指标过剩：现有{high_school_counter[key]}，上限为{limit_dict[key]}")
    else:
        print(fr"{key}指标满足")

print("")

for key in area_counter.keys():
    if area_counter[key] > limit_dict[key]:
        print(fr"{key}指标不满足：现有{area_counter[key]}，上限为{limit_dict[key]}")
    elif area_counter[key] < limit_dict[key]:
        print(fr"{key}指标过剩：现有{area_counter[key]}，上限为{limit_dict[key]}")
    else:
        print(fr"{key}学片指标满足")

# 检查所有定期奖励人员是否师德考核合格及以上
id_list = [item[3] for item in read_xlsx_to_list(file_path=fr"2026.03.17/1.xlsx")]  # 读取所有嘉奖的身份证
check_moral_dict = {item[4]: item[9] for item in
                    read_xlsx_to_list(file_path=fr"2026.03.16/1.xlsx")}  # 读取所有师德考核的结果，首项为身份证，次项为考核结果

for item in data:
    if check_moral_dict.get(item[3], "") not in ["合格", "优秀"]:
        print(item[1], item[5], item[2], item[3])
