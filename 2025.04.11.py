from func import *

school_list = "广州市白云区金沙第二小学 广州市白云区金沙小学 广州市白云区沙凤小学 广州市白云区横沙小学 ".split()
#  ("交流结束时间" == "无" or cast(substring("交流结束时间", 1, 4) as integer) <= 2016) and cast(substring("入现单位时间",1,4) as integer) <= 2016
data = execute_sql_sentence(
    sentence=f'select "交流结束时间" from teacher_data_0 where "采集年份" == 2024 '
             f'and "校名" in ({', '.join([f'"{s}"' for s in school_list])}) '
             f'and "2024年9月编制所在学段" in ("初中","小学") '
             f'and(cast(substring("入现单位时间",1,4) as integer) >= 2020 and "交流结束时间" == "无" or cast(substring("入现单位时间",1,4) as integer) <= 2016 and ("交流结束时间" == "无" or cast(substring("交流结束时间", 1, 4) as integer) <= 2016))'
)

print(len(data))

print(
    len(execute_sql_sentence(
        sentence=f'select "交流结束时间" from teacher_data_0 where "采集年份" == 2024 and "校名" in ({', '.join([f'"{s}"' for s in school_list])}) and "2024年9月编制所在学段" in ("初中","小学")'
    ))
)
