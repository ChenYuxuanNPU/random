from func import *

school_list = del_tuple_in_list(
    data=execute_sql_sentence(
        sentence=f'select distinct "校名" from teacher_data_0 where "采集年份" == "2024" and "区域" != "直管"'
    )
)

# ({', '.join([f'"{year}"' for year in year_list])})

output = {area: {} for area in ["新市", "石井", "永平", "江高", "人和", "太和", "钟落潭"]}

temp = execute_sql_sentence(
    sentence=f'select "区域", count(*) from teacher_data_0 where "采集年份" == "2024" and "区域" != "直管" group by "区域"'
)

for item in temp:
    output[item[0]]["公办在编"] = item[1]

temp = execute_sql_sentence(
    sentence=f'select "区域", count(*) from teacher_data_1 where "采集年份" == "2024" and "区域" != "直管" and "校名" in ({', '.join([f'"{school}"' for school in school_list])}) group by "区域"'
)

for item in temp:
    output[item[0]]["公办编外"] = item[1]

temp = execute_sql_sentence(
    sentence=f'select "区域", count(*) from teacher_data_1 where "采集年份" == "2024" and "区域" != "直管" and "校名" not in ({', '.join([f'"{school}"' for school in school_list])}) group by "区域"'
)

for item in temp:
    output[item[0]]["民办教师"] = item[1]

print(output)

