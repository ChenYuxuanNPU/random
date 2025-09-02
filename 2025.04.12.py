"""
教师问卷结果统计
"""

import copy
import json

from func import *

# 读取JSON文件
with open('answer_teacher.json', 'r', encoding='utf-8') as file:
    json_data = dict(json.load(file))

raw_data = read_xlsx_to_list(file_path="1.xlsx")

output_dict = {}

sum_txt = {"合计": copy.deepcopy(json_data)}  # 单单用来算合计的txt

question_list = list(json_data.keys())  # 不包含校名

answer_list = raw_data[1:]  # 去除首行

for ans in answer_list:

    school_name = ans[0]
    if school_name not in output_dict.keys():
        output_dict[school_name] = copy.deepcopy(json_data)

    for i in range(1, len(ans)):
        if ans[i] in output_dict[school_name][question_list[i - 1]].keys():
            output_dict[school_name][question_list[i - 1]][ans[i]] += 1
        else:
            output_dict[school_name][question_list[i - 1]][ans[i]] = 1

        if ans[i] in sum_txt["合计"][question_list[i - 1]].keys():
            sum_txt["合计"][question_list[i - 1]][ans[i]] += 1
        else:
            sum_txt["合计"][question_list[i - 1]][ans[i]] = 1

        output_dict[school_name][question_list[i - 1]]["总数"] += 1
        sum_txt["合计"][question_list[i - 1]]["总数"] += 1

# 生成txt文档
for school_name in output_dict.keys():

    school_data = dict(output_dict[school_name])

    with open(f"output_teacher/{school_name}.txt", mode="w", encoding="UTF-8") as f:
        print(f"{school_name}教师问卷数据", file=f)

        count = 1
        for question in question_list[:-3]:  # todo

            print(f"题目{count}：{question}", file=f)

            ans_title = ["A", "B", "C", "D"]
            title_count = 0
            for answer in school_data[question]:

                if answer != "总数":
                    print(
                        f"答案{ans_title[title_count]}：{answer}， 选择人数：{school_data[question][answer]}， 占比：{str(100 * round(school_data[question][answer] / school_data[question]['总数'], 4))[:5]}%",
                        file=f)
                    title_count += 1

            print("", file=f)
            count += 1

        for question in question_list[-3:]:  # todo
            print(f"题目{count}：{question}， 回答总数：{school_data[question]['总数']}", file=f)

            for answer in school_data[question]:

                if answer != "总数":
                    print(f"答案：{answer}， 回答人数：{school_data[question][answer]}", file=f)

            print("", file=f)

            count += 1

# 生成合计txt文档
# 生成txt文档
for school_name in ['合计']:

    school_data = dict(sum_txt[school_name])

    with open(f"output_teacher/{school_name}.txt", mode="w", encoding="UTF-8") as f:
        print(f"{school_name}教师问卷数据", file=f)

        count = 1
        for question in question_list[:-3]:  # todo

            print(f"题目{count}：{question}", file=f)

            ans_title = ["A", "B", "C", "D"]
            title_count = 0
            for answer in school_data[question]:

                if answer != "总数":
                    print(
                        f"答案{ans_title[title_count]}：{answer}， 选择人数：{school_data[question][answer]}， 占比：{str(100 * round(school_data[question][answer] / school_data[question]['总数'], 4))[:5]}%",
                        file=f)
                    title_count += 1

            print("", file=f)
            count += 1

        for question in question_list[-3:]:  # todo
            print(f"题目{count}：{question}， 回答总数：{school_data[question]['总数']}", file=f)

            for answer in school_data[question]:

                if answer != "总数":
                    print(f"答案：{answer}， 回答人数：{school_data[question][answer]}", file=f)

            print("", file=f)

            count += 1

# 生成xlsx文件
output = [["校名", "问题", "A选项人数", "A选项占比", "B选项人数", "B选项占比", "C选项人数", "C选项占比", "D选项人数",
           "D选项占比"]]

sum_stat = {f"问题{i}": {f"{chara}": 0 for chara in ["A", "B", "C", "D"]} for i in range(1, 18)}
# todo

for school_name in output_dict.keys():

    school_data = dict(output_dict[school_name])

    count = 1

    for question in question_list[:-3]:  # todo
        temp = []

        if len(list(school_data[question].keys())) <= 5:

            chara_flag = 0
            ans_title = ["A", "B", "C", "D"]
            for ans in school_data[question].keys():
                if ans != "总数":
                    temp.extend([school_data[question][ans],
                                 f'{str(round(school_data[question][ans] / school_data[question]["总数"] * 100, 4))[:5]}%'])
                    sum_stat[f"问题{count}"][ans_title[chara_flag]] += school_data[question][ans]
                    chara_flag += 1

            temp = [school_name, f"问题{count}"] + temp
            output.append(temp)
            count += 1

for i in sum_stat.keys():
    temp = ["合计", i]

    for k in sum_stat[i].keys():
        temp.extend([sum_stat[i][k], f'{str(round(sum_stat[i][k] / sum(sum_stat[i].values()) * 100, 4))[:5]}%'])
    print(temp)
    output.extend([temp])

print(output)
save_excel(two_dimension_list=output, excel_name="output_teacher/合计表格")

temp = {s: {} for s in ["广州市白云区同和中学", "广州市白云区东平学校"]}
for school in ["广州市白云区同和中学", "广州市白云区东平学校"]:
    count = 1
    with open(rf"0416/{school}-教师.txt", "w", encoding='UTF-8') as f:
        data = output_dict[school]

        for qes in data.keys():
            print(data[qes])
            if len(list(data[qes].keys())) <= 5:
                print(f"问题{count}：“{qes}”中，", end="", file=f)
                count += 1

                for ans in data[qes].keys():
                    if ans != "总数" and data[qes][ans] > 0:
                        print(
                            f"{data[qes][ans]}位教师认为“{ans}”，占比{str(round(data[qes][ans] / data[qes]['总数'] * 100, 4))[:5]}%",
                            file=f, end=";")

            else:
                for ans in data[qes].keys():
                    if ans != "总数":
                        if qes in temp[school].keys():
                            temp[school][qes].append(ans)

                        else:
                            temp[school][qes] = []
                            temp[school][qes].append(ans)

            print("", file=f)
            print("", file=f)

for key in temp.keys():
    print(key)
    print(temp[key])
