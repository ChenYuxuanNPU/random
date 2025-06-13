from func import *

data = execute_sql_sentence(
    sentence=f'select "校名","学校类型","姓名","参加工作前毕业院校","参加工作前毕业时间","最高学历毕业院校","最高学历毕业时间","入编时间","主教学科" from teacher_data_0 where "采集年份" == "2024" and ("最高学历毕业院校" == "湖南师范大学" or "参加工作前毕业院校代码" == "10542" or "参加工作前毕业院校" == "湖南师范大学")'
)

print(data)

save_excel(two_dimension_list=data, excel_name="湖南师范大学")
