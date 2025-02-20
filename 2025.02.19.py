from func import *

school_list = ["广州市白云区谢家庄小学",
               "广州市白云区大岡小学",
               "广州市白云区石湖小学",
               "广州市白云区长红小学",
               "广州市白云区红星小学",
               "广州市白云区太和第二小学",
               "广州市白云区鹤边镇泰小学",
               "广州市白云区龙江小学",
               "广州市白云区潭岗小学",
               "广州市白云区人和镇第七小学",
               "广州市白云区永兴小学",
               "广州市白云区龙归学校",
               "广州市第七十三中学",
               "广州市第七十中学",
               "广州市白云区广州空港实验中学",
               ]

period_list = ["小学", "小学", "小学", "小学", "小学", "小学", "小学", "小学", "小学", "小学", "小学", "小学", "小学",
               "初中", "初中"]

output = {}

for i in range(len(school_list)):
    # result = del_tuple_in_list(
    #     data=execute_sql_sentence(
    #         sentence=f'select "教师资格学科" from teacher_data_0 where "采集年份" = "2024" and "任教学段" = "{period_list[i]}" and "校名" = "{school_list[i]}"'
    #     )
    # )

    result = (
        del_tuple_in_list(
            data=execute_sql_sentence(
                sentence=f'select "教师资格学科" from teacher_data_1 where "采集年份" = "2024" and "任教学段" = "{period_list[i]}" and "校名" = "{school_list[i]}"'
            )
        )
    )

    #
    # result.extend(
    #     del_tuple_in_list(
    #         data=execute_sql_sentence(
    #             sentence=f'select "教师资格学科" from teacher_data_1 where "采集年份" = "2024" and "任教学段" = "{period_list[i]}" and "校名" = "{school_list[i]}"'
    #         )
    #     )
    # )

    print(school_list[i])
    print(result)
    print("")

# save_excel(two_dimension_list=[[item] for item in school_list], excel_name="2025.02.19")
