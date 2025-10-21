"""
用于统计某一个学生在班级、学校、区层面的排名
"""
from func import *


def extract_columns(matrix, column_indices):
    """提取二维列表的指定列"""
    return [[row[i] for i in column_indices] for row in matrix]


# 用于保存每个科目总分，用于计算等级
subject_max_score_dict = {
    "语文": 120,
    "数学": 120,
    "英语": 120,
    "道法": 90,
    "物理": 100,
    "化学": 100,
    "生物": 100,
    "地理": 100,
    "历史": 90,
    "音乐": 100,
    "体育": 100,
    "美术": 100,
    "五科总分": 540,
    "七科总分": 740,
    "六科总分": 640,
    "信息": 100,
}

stu_name = ""
stu_class_id = ""
stu_school_id = ""

data = read_xlsx_to_list(file_path=fr"C:\Users\1012986131\Desktop\python\考试数据统计\成绩原始数据\242224.xlsx", )[1:]

title = ["学校代码", "班级代码", "姓名", "五科总分", "七科总分", "语文", "数学", "英语", "道法", "生物", "地理", "历史",
         "音乐", "美术", "信息", "体育"]
columns = [2, 4, 6, 10, 11, 12, 15, 18, 21, 24, 27, 30, 33, 36, 40, 43]

data = [[item[i] for i in columns] for item in data]

subjects = ["五科总分", "七科总分", "语文", "数学", "英语", "道法", "生物", "地理", "历史",
            "音乐", "美术", "信息", "体育"]

for location, subject in enumerate(title):

    if subject in subjects:

        class_rank = get_descending_rank(lst=[item[location] for item in data if
                                              item[location] and item[location] > 0 and str(item[0]) == str(
                                                  stu_school_id)],
                                         value=[item for item in data if item[2] == stu_name][0][location])
        district_rank = get_descending_rank(
            lst=[item[location] for item in data if item[location] and item[location] > 0],
            value=[item for item in data if item[2] == stu_name][0][location])

        print(subject + "：")
        print(f"得分：{[item for item in data if item[2] == stu_name][0][location]}/{subject_max_score_dict[subject]}")
        print(
            f"年级排名：{class_rank}/{len([item[location] for item in data if item[location] and item[location] > 0 and str(item[0]) == str(stu_school_id)])}")
        print(
            f"区排名：{district_rank}/{len([item[location] for item in data if item[location] and item[location] > 0])}")


    else:
        continue
