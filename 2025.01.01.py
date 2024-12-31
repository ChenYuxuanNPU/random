from func import *


def gen_info_dict(data: list[list | tuple]) -> dict:
    output = {
        "平均年龄": round(sum([row[0] for row in data]) / len([row[0] for row in data]), 2),
        "29岁及以下": 0,
        "30-39岁": 0,
        "40-49岁": 0,
        "50岁及以上": 0,
        "男57及以上": 0,
        "女52及以上": 0,
        "近三年退休（上两项求和）": 0
    }

    for item in data:
        if item[0] <= 29:
            output["29岁及以下"] += 1
        if 30 <= item[0] <= 39:
            output["30-39岁"] += 1
        if 40 <= item[0] <= 49:
            output["40-49岁"] += 1
        if item[0] >= 50:
            output["50岁及以上"] += 1
        if item[0] >= 57 and item[1] == "男":
            output["男57及以上"] += 1
            output["近三年退休（上两项求和）"] += 1
        if item[0] >= 52 and item[1] == "女":
            output["女52及以上"] += 1
            output["近三年退休（上两项求和）"] += 1

    return output


school_list = del_tuple_in_list(
    data=execute_sql_sentence(
        sentence=f'select distinct "校名" from teacher_data_0_2024'
    )
)

age_dict = {}
check_dict = {}
for school in school_list:
    age_list = []
    id_list = execute_sql_sentence(
        sentence=f'select "身份证号","性别" from teacher_data_0_2024 where "校名" = "{school}"'
    )

    for id_set in id_list:
        age_list.append([get_age_from_citizen_id(citizen_id=id_set[0], year="2024", month=12, day=31), id_set[1]])

    check_dict[school] = age_list
    age_dict[school] = gen_info_dict(data=age_list)

print(check_dict)
print(age_dict)


#
# with open('data.json', 'w', encoding='utf-8') as json_file:
#     json.dump(age_dict, json_file, ensure_ascii=False, indent=4)
#
# for school in age_dict.values():


def gen_check_excel(dict1):
    output = []
    for school in dict1.keys():

        temp = [school]

        for data in dict1[school]:
            for item in data:
                temp.append(item)

        output.append(temp)

    save_excel(two_dimension_list=output, excel_name="检查用")


gen_check_excel(dict1=check_dict)


def gen_statistics(dict1: dict):
    output = [[""] + list({
                              "平均年龄": 1,
                              "29岁及以下": 0,
                              "30-39岁": 0,
                              "40-49岁": 0,
                              "50岁及以上": 0,
                              "男57及以上": 0,
                              "女52及以上": 0,
                              "近三年退休（上两项求和）": 0
                          }.keys())]

    for school in dict1.keys():
        temp = [school]

        for _, values in dict1[school].items():
            temp.append(values)

        output.append(temp)

    save_excel(two_dimension_list=output, excel_name="统计结果")


gen_statistics(dict1=age_dict)
