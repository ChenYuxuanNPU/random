"""
义务教育优质均衡国测数据统计
表一:学校，学片，均分达到度，后30%人数，后30%人数占比，占比排名
表二:小题分
表三:学片，学校，班级，学生姓名
"""

from func import *


def get_rank(score: int | float, score_list: list[int | float]) -> int:
    """
    用于返回某一个成绩在成绩列表中的排名，取高排名
    :param score: 给定的成绩
    :param score_list: 成绩列表（由低到高）
    :return: 排名
    """
    for i, item in enumerate(sorted(score_list)[::-1]):
        if score == item:
            return i + 1

    return -1


test_data = read_xlsx_to_list(file_path=fr"C:\Users\1012986131\Desktop\python\random\省测数据.xlsx", )[1:]

subject_list = read_xlsx_to_list(file_path=fr"C:\Users\1012986131\Desktop\python\random\省测数据.xlsx", )[0][4:]

school_list = list(set([item[2] for item in
                        read_xlsx_to_list(file_path=fr"C:\Users\1012986131\Desktop\python\random\国测数据.xlsx", )[
                            1:]]))

subjects = {item: i + 4 for i, item in enumerate(subject_list)}

for subject in subjects:

    subject_scores = sorted([item[subjects[subject]] for item in test_data if item[subjects[subject]] != -1])
    subject_scores_avg = sorted([item[subjects[subject]] for item in test_data if item[subjects[subject]] > 0])
    threshold = subject_scores[int(len(subject_scores) * 0.3)]

    output_1 = {item: [] for item in school_list}
    output_1_list = [
        ["学校", "学片", "达到度", "后30%人数", "后30%占比（数值）", "后30%占比（文本）", "后30%占比排名", "是否后30%学校"]]

    for school in output_1.keys():
        output_1[school].append(school[:3] if school[:3] != "钟落潭" else "钟落潭镇")

    for school in output_1.keys():
        # 均分：sum(item[subjects[subject]] for item in test_data if item[subjects[subject]] > 0 and item[2] == school) / len([item[subjects[subject]] for item in test_data if item[subjects[subject]] > 0 and item[2] == school])
        # 区均分：sum(subject_scores_avg) / len(subject_scores_avg)
        if len(
                [item[subjects[subject]] for item in test_data if
                 item[subjects[subject]] > 0 and item[2] == school]) > 0:
            output_1[school].append(f'{round(100 * (sum(
                item[subjects[subject]] for item in test_data if item[subjects[subject]] > 0 and item[2] == school) / len(
                [item[subjects[subject]] for item in test_data if item[subjects[subject]] > 0 and item[2] == school])) / (
                                                     sum(subject_scores_avg) / len(subject_scores_avg)), 2)}%')
        else:
            output_1[school].append(-1)

    for school in output_1.keys():
        output_1[school].append(len([item for item in test_data if
                                     item[2] == school and item[subjects[subject]] <= threshold and item[
                                         subjects[subject]] != -1]))

    for school in output_1.keys():
        if len(
                [item for item in test_data if item[2] == school and item[subjects[subject]] != -1]) > 0:
            output_1[school].append(round(
                len([item for item in test_data if
                     item[2] == school and item[subjects[subject]] <= threshold and item[
                         subjects[subject]] != -1]) / len(
                    [item for item in test_data if item[2] == school and item[subjects[subject]] != -1]), 5))
        else:
            output_1[school].append(-1)

    for school in output_1.keys():
        if len(
                [item for item in test_data if item[2] == school and item[subjects[subject]] != -1]) > 0:
            output_1[school].append(
                f"{round(100 * len([item for item in test_data if item[2] == school and item[subjects[subject]] <= threshold and item[subjects[subject]] != -1]) / len(
                    [item for item in test_data if item[2] == school and item[subjects[subject]] != -1]), 2)}%")
        else:
            output_1[school].append(-1)

    back_30_ratio_list = [item[-2] for item in output_1.values() if item[-2] != -1]

    for school in output_1.keys():
        output_1[school].append(get_rank(output_1[school][-2], back_30_ratio_list))

    for school in output_1.keys():
        if output_1[school][-1] <= 0.3 * len(school_list):
            output_1[school].append("是")
        else:
            output_1[school].append("否")

    for key, value in output_1.items():
        output_1_list.append([key] + [item for item in value])

    output_1_list = [output_1_list[0]] + sorted(output_1_list[1:], key=lambda x: x[6])

    save_excel(two_dimension_list=output_1_list, excel_name=f'output/{subject}学校数据')

    output_2 = [["学号", "姓名", "学校", "片镇", f"{subject}成绩", "30%临界成绩"]]

    for item in test_data:
        if item[subjects[subject]] <= threshold and item[subjects[subject]] != -1:
            output_2.append(item[:4] + [item[subjects[subject]], threshold])

    output_2 = [output_2[0]] + sorted(output_2[1:], key=lambda x: (x[3], x[2], x[4]))

    save_excel(two_dimension_list=output_2, excel_name=f"output/{subject}考生列表")
