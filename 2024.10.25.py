import os
import re
import shutil
import pandas as pd


def read_xlsx(file_path: str, sheet_name: str) -> list:
    # 读取Excel文件
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    print(df)

    # 将DataFrame转换为列表（每个元素是一行，行内是列表形式的数据）
    return df.values.tolist()


def split_string(s):
    # 使用正则表达式按照空格或加号分割字符串
    return re.split(r'[ +-_-＋、.]', s)


def get_all_files(directory):
    # 初始化一个空列表来存储文件名
    file_list = []
    # 遍历指定目录下的所有文件和文件夹
    for root, dirs, files in os.walk(directory):
        # 将文件名添加到列表中
        for file in files:
            file_list.append(file)
    return file_list


current_file_name_list = get_all_files(directory=r"C:\Users\1012986131\Desktop\python\random\2024.10.25\doc_list")
print(current_file_name_list)
print("")

output_file_name_list = read_xlsx(file_path=r"/2024.10.25/file_name_list.xlsx", sheet_name="Sheet1")
print(len(output_file_name_list))
for current_file_name in current_file_name_list:
    if_found = False
    output_info = []

    for split_file_name in split_string(current_file_name):
        for output_file_name in output_file_name_list:
            if split_file_name in output_file_name[2] and split_file_name is not None and split_file_name != "":

                if_found = True
                print(f"{current_file_name} -> {output_file_name[2]}")
                output_info = output_file_name

    if not if_found:
        print("")
        print(current_file_name)
        print("")

    else:
        try:
            shutil.copy2(fr"C:\Users\1012986131\Desktop\python\random\2024.10.25\doc_list\{current_file_name}",fr"C:\Users\1012986131\Desktop\python\random\2024.10.25\output\{output_info[0]}\{output_info[1]}.docx")
            print(fr"正在移动：{current_file_name} -> {output_info[0]}\{output_info[1]}.docx")
        except Exception as e:
            print(f"{e}")


