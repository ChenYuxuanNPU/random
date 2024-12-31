from func import *

result = read_xlsx_to_list(file_path=r"*.xlsx", sheet_name="Sheet1")
print(result)

output = []
for item in result:
    temp = execute_sql_sentence(sentence=f'select "校名", "籍贯", "政治面貌", "参加工作前毕业院校", "参加工作前所学专业", "主教学科" from teacher_data_0_2024 where "姓名" = "{item[1]}" and "身份证号" = "{item[0]}"')

    if not temp:
        print(item)
    else:
        output.append([item[0], item[1]] + list(temp[0]))

print(output)

# save_excel(two_dimension_list=output)



