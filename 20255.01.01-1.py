import copy

from func import *

list0 = del_tuple_in_list(
    data=[('高级教师',), ('未取得职称',), ('二级教师',), ('一级教师',), ('三级教师',), ('正高级教师',)])


def gen_check_excel(dict1: dict):
    output = []

    for school in dict1.keys():
        temp = [school]

        for item in dict1[school]:
            temp.append(item)

        output.append(temp)

    save_excel(two_dimension_list=output, excel_name="职称检查用")

    return None


def gen_statistics(dict1: dict):
    output = [[""] + [item for item in list0 + ["其他"]]]

    for school in dict1.keys():
        output.append([school, dict1[school]["高级教师"], dict1[school]["未取得职称"], dict1[school]["二级教师"],
                       dict1[school]["一级教师"], dict1[school]["三级教师"], dict1[school]["正高级教师"],
                       dict1[school]["其他"], ])

    save_excel(two_dimension_list=output, excel_name="职称统计结果")


if __name__ == '__main__':
    school_list = del_tuple_in_list(
        data=execute_sql_sentence(
            sentence=f'select distinct "校名" from teacher_data_0_2024'
        )
    )

    output = {}
    check_dict = {}
    for school in school_list:
        temp = {item: 0 for item in list0 + ["其他"]}
        print(temp)
        list1 = del_tuple_in_list(
            execute_sql_sentence(sentence=f'select "最高职称" from teacher_data_0_2024 where "校名" = "{school}"'))

        check_dict[school] = copy.deepcopy(list1)

        for item in list1:
            if item in temp.keys():
                temp[item] += 1
            else:
                temp["其他"] += 1

        output[school] = copy.deepcopy(temp)

    # print(check_dict)
    gen_check_excel(check_dict)
    # print(output)
    gen_statistics(output)
