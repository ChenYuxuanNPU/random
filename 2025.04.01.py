from func import *

info_list = execute_sql_sentence(
    sentence=f'select "校名","姓名","主教学科","兼教学科","任教学段" from teacher_data_0 where "采集年份" == "2024"'
)

output_0 = [["学校", "姓名", "主教学科", "兼教学科", "任教学段"]]
output_1 = [["学校", "姓名", "主教学科", "兼教学科", "任教学段"]]

for item in info_list:
    if item[2] in ["体育", "音乐", "美术"]:
        output_0.append(item)
    else:
        for chara in "体音乐美球":
            if item[3] and chara in item[3]:
                output_1.append(item)
                break

save_excel(two_dimension_list=output_0, excel_name="主教音体美")
save_excel(two_dimension_list=output_1, excel_name="兼教音体美")
