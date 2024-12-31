from func import *


def get_educational_background_order() -> dict:
    """
    学历排序
    :return:
    """

    return {
        '博士研究生': 1, '硕士研究生': 2, '本科': 3, "专科": 4, "高中": 5, "高中及以下": 6,
        "中师": 7, "中专（非师范）": 8, "中专": 9, "初中": 10, None: 11
    }


data_0 = sorted(
    execute_sql_sentence(
        sentence=fr'select "最高学历", count(*) from teacher_data_0_2024 group by "最高学历" order by count(*) desc'
    ), key=lambda x: get_educational_background_order()[x[0]]
)

print(data_0)

data_1 = sorted(
    execute_sql_sentence(
        sentence=fr'select "最高学历", count(*) from teacher_data_1_2024 group by "最高学历" order by count(*) desc'
    ), key=lambda x: get_educational_background_order()[x[0]]
)
print(data_1)
