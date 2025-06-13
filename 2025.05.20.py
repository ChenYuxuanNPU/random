from func import *

school = "广州市白云区石井中学"

data = [("姓名", "性别", "民族", "主教学科", "教师资格学段")]

data.extend(
    execute_sql_sentence(
        sentence=f'select "姓名","性别","民族","主教学科","教师资格学段" from teacher_data_0 where "采集年份" == "2024" and "校名" == "{school}"'
    )
)

data.extend(
    execute_sql_sentence(
        sentence=f'select "姓名","性别","民族","主教学科","教师资格学段" from teacher_data_1 where "采集年份" == "2024" and "校名" == "{school}"'
    )
)

print(data)

for i in range(1,len(data)):
    data[i] = list(data[i])

    data[i][4] += "教师资格"

print(data)
print(len(data))

save_excel(two_dimension_list=data,
           excel_name=school)
