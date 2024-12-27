from func import *

with open('1.txt', 'r', encoding='UTF-8') as file:
    # 读取文件的所有行，并将它们作为列表的元素
    lines = []
    for line in file:
        stripped_line = line.strip()
        lines.append(stripped_line)


print(len(lines))

for id in lines:
    school_id = execute_sql_sentence(sentence=f'select "参加工作前毕业院校代码" from teacher_data_0_2024 where "身份证号" = "{str(id)}"')
    print(school_id)