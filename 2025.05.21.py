from func import *

school = "广州市白云区同和中学"

data = [("姓名", "性别", "民族", "主教学科", "最高学历")]

data.extend(
    execute_sql_sentence(
        sentence=f'select "姓名","性别","民族","主教学科","最高学历" from teacher_data_0 where "采集年份" == "2024" and "校名" == "{school}"'
    )
)

data.extend(
    execute_sql_sentence(
        sentence=f'select "姓名","性别","民族","主教学科","最高学历" from teacher_data_1 where "采集年份" == "2024" and "校名" == "{school}"'
    )
)

print(data)

print(data)

print(len(data))

save_excel(two_dimension_list=data,
           excel_name=school)
