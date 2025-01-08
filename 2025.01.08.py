"""
六中实验中学、七十三中、人和一小、二小、五小、六小、七小、空港实验小学、六中实验小学
"""

from func import *

for school in ["广州市白云区六中实验中学", "广州市第七十三中学", "广州市白云区人和镇第一小学",
               "广州市白云区人和镇第二小学", "广州市白云区人和镇第五小学", "广州市白云区人和镇第六小学",
               "广州市白云区人和镇第七小学", "广州市白云区广州空港实验小学", "广州市白云区六中实验小学"]:
    #  print(execute_sql_sentence(sentence=f'select count(*) from teacher_data_0_2024 where "校名" = "{school}"'))

    id_list = del_tuple_in_list(
        execute_sql_sentence(
            f'select "身份证号" from teacher_data_0_2024 where "校名" = "{school}"'
        )
    )

    age_list = [get_age_from_citizen_id(citizen_id=str(id), year="2025", month=1, day=8) for id in id_list]

    print(f'{school}平均年龄为：{round(sum(age_list) / len(age_list), 2)}岁')
